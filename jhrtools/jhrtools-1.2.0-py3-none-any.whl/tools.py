#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2022/3/9 14:52
@Author   : ji hao ran
@File     : tools.py
@Project  : pkgDev
@Software : PyCharm
"""
import inspect
import re
import time
import simplejson as json
from tqdm import tqdm
import pandas as pd
import numpy as np
from pandas import DataFrame, Timestamp
from functools import partial
from pathos.pools import ProcessPool, ThreadPool
from functools import reduce
from itertools import product
from typeguard import typechecked
from typing import Union
import platform
import netifaces
import socket

__all__ = ['Jet', 'JetTimeStamp', 'JetEncoder', 'get_host_ip']


class Jet:
    """
    jet基类
    """

    def __new__(cls, *args, **kwargs):
        """为类添加参数检查功能"""
        return super().__new__(typechecked(cls))

    @staticmethod
    def merge_dict(*args: dict) -> dict:
        """合并多个字典

        :param args: 字典
        :return: 合并后的字典，重复key会覆盖
        """
        return dict(reduce(lambda l1, l2: l1 + l2, map(lambda d: list(d.items()), args)))

    @staticmethod
    def filter_dict(obj: dict, conf: str = None) -> dict:
        """字典筛选过滤

        :param obj: 字典
        :param conf: 过滤条件语句，字典的key用k表示，value用v表示
        :return: 筛选后的字典
        """
        if conf:
            if 'k' not in conf and 'v' not in conf:
                raise ValueError(f'parameter "filter" need contain "k" or "v"!')
            return {k: v for k, v in obj.items() if (lambda k, v: eval(conf))(k, v)}
        else:
            return obj

    @staticmethod
    def flat(obj) -> list:
        """扁平化嵌套序列

        :param obj: 序列
        :return: 扁平化后的列表
        """
        return list(pd.core.common.flatten(obj))

    @staticmethod
    def groupbyprod(*args: DataFrame):
        """数据框按行求笛卡尔积分组

        :param args: 多个数据框
        :return: 分组数据框
        """
        # reset index
        # _df = [v.set_index(v.index.map(lambda x: f'{i}{sep}{x}')) for i, v in enumerate(args)]
        # merge dataframe
        _merge = pd.concat(args)
        # product all dataframe index
        _prod = list(product(*map(lambda x: x.T, args)))
        # repeat index
        _repeat = np.repeat(_prod, len(args), axis=0)
        # sub dataframe
        _sub_df = _merge.loc[[j for i in _prod for j in i]]
        # rename index sub dataframe
        _sub_df.set_axis(_repeat, inplace=True)
        # group
        g_df = _sub_df.groupby(level=0)
        return g_df

    @staticmethod
    def check_df(*args: DataFrame, row: int = None, col: int = None):
        """
        检查数据框是否合法

        :param args: 数据框
        :param row: 行数目标值
        :param col: 列数目标值
        :return: True数据框合法
        """
        legal = list()
        for i in args:
            if i.empty:
                legal.append(False)
            else:
                is_row = False if row and i.shape[0] != row else True
                is_col = False if col and i.shape[1] != col else True
                legal.append(all([is_row, is_col]))
        if all(legal):
            return True
        else:
            print('DataFrame is illegal!')
            return False

    def check(self, *statement: str, scope=None, silent=False):
        """条件语句检查

        :param statement: 约束条件语句
        :param scope: 约束条件作用域
        :param silent: 不满足约束条件时，是否保存，默认报错
        :return: True,满足约束条件；False,不满足约束条件
        """
        scope = scope if scope else locals()
        result = []
        for s in statement:
            try:
                r = eval(s, globals(), scope)
            except Exception:
                raise Exception
            if not r and not silent:
                raise ValueError(f'{self.meta} statement "{s}" not satisfied')
            result.append(r)
        return True if all(result) else False

    @property
    def _msg(self):
        """信息"""
        class_name = self.__class__.__name__
        now = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        return f'{now} {class_name}'

    @property
    def meta(self):
        """运行头信息"""
        return f'{self._msg} {inspect.stack()[1][3]}'

    @property
    def fail(self):
        """运行失败信息"""
        return f'{self._msg} {inspect.stack()[1][3]} FAIL'

    @property
    def success(self):
        """运行成功信息"""
        return f'{self._msg} {inspect.stack()[1][3]} SUCCESS'


class JetEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        重写json模块JSONEncoder类中的default方法
        """
        # pandas naive Timestamp类型数据转为毫秒时间戳
        if isinstance(obj, pd.Timestamp):
            return JetTimeStamp(obj).ms
        # np整数转为内置int
        elif isinstance(obj, np.integer):
            return int(obj)
        # np浮点数转为内置float
        elif isinstance(obj, np.floating):
            return float(obj)
        # 字节串转为字符串
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        # series转list
        elif isinstance(obj, pd.Series):
            return obj.to_list()
        else:
            # return json.JSONEncoder.default(obj)
            return super().default(obj)


class JetTimeStamp(Jet):
    # 本地时区
    tz = 'Asia/shanghai'
    # 相对时间偏移和对齐字符模式
    pattern = '-?\\d*[A-Z]'
    # 相对时间允许模式
    allow_pattern = [pattern, pattern + ':', ':' + pattern, pattern + ':' + pattern]

    def __init__(self, obj: Union[float, str, Timestamp, np.integer] = None, **kwargs):
        """
        jet自定义时间戳格式，可转各种自定义时间格式为时间戳。
        支持输入：
        1. numpy integer/int/float: 绝对时间
        2. str: 绝对时间：'%Y%m%d%H:%M:%S',相对时间：'-3D:-H'
        3. None: 当前时间
        4. pd.TimeStamp: 绝对时间

        :param obj: 时间，JetTimeStamp支持的输入类型
        :param kwargs: 时间的其他关键字参数,绝对时间时，为TimeStamp的关键字参数，相对时间时为base,相对时间的基准
        """
        self.obj = obj
        self.kwargs = kwargs
        self.now = pd.Timestamp.now(self.tz)

    def __str__(self):
        return self.ts.__str__()

    def _get_number_unit(self, value: str, offset=True):
        """
        获取offset/align value字符串中的数值和单位
        :param value: 字符串
        :param offset: 是否是偏移字符串
        :return:
        """
        # 负号
        minus_str = re.findall('^-', value)
        # 数值
        n_str = re.findall('\\d+', value)
        # 单位
        u_str = re.findall('[A-Z]$', value)
        # 单位检查
        self._unit_check(u_str[0], offset)
        # 无数值设置为1
        n = int(n_str[0]) if n_str else 1
        # 有负号添加负号
        n = -n if minus_str else n
        # 更新value
        value_update = str(n) + u_str[0]
        # 返回
        return n, value_update

    @staticmethod
    def _unit_check(unit: str, offset=True):
        """
        对单位做检查
        :param unit:
        :param offset:
        :return: 错误信息
        """
        offset_unit = ['T', 'H', 'D', 'W', 'M', 'Y']
        align_unit = ['T', 'H', 'D', 'M', 'Y']
        if offset:
            if unit not in offset_unit:
                raise ValueError('OFFSET unit must be one of {},bug get {} !'.format(str(offset_unit), unit))
        else:
            if unit not in align_unit:
                raise ValueError('ALIGN unit must be one of {},bug get {} !'.format(str(align_unit), unit))

    def _add_offset(self, x, offset_value: str):
        """
        给基准时间x增加偏移量
        :param x: pandas TimeStamp,基准时间
        :param offset_value: 偏移量
        :return:
        """
        offset_n, offset_value = self._get_number_unit(offset_value)
        if 'M' in offset_value:
            x_offset = x + pd.DateOffset(months=offset_n)
        else:
            x_offset = x + pd.Timedelta(offset_value)
        return x_offset

    def _add_align(self, x, align_value: str):
        """
        对时间x对齐操作
        :param x: pandas TimeStamp,时间
        :param align_value: 对齐量
        :return:
        """
        align_n, align_value = self._get_number_unit(align_value, offset=False)
        if align_n < 0:
            if 'M' in align_value:
                x_align = x.date() + pd.offsets.MonthBegin(align_n)
            elif 'Y' in align_value:
                x_align = x.date() + pd.offsets.YearBegin(align_n)
            else:
                x_align = x.ceil(align_value)
        else:
            if 'M' in align_value:
                x_align = x.date() + pd.offsets.MonthEnd(align_n)
            elif 'Y' in align_value:
                x_align = x.date() + pd.offsets.YearEnd(align_n)
            else:
                x_align = x.ceil(align_value)
        return x_align

    def _absolute(self, obj, **kwargs):
        """
        绝对时间转为时间戳
        :param obj: 绝对时间
        :return: 毫秒时间戳
        """
        if isinstance(obj, (float, int, np.integer)):
            digits = len(int(obj).__str__())
            if digits == 10:  # 秒
                return pd.Timestamp(obj, unit='s', tz=self.tz)
            elif digits == 13:  # 毫秒
                return pd.Timestamp(obj, unit='ms', tz=self.tz)
            else:
                return pd.Timestamp(obj, tz=self.tz, **kwargs)
        elif isinstance(obj, pd.Timestamp):
            if obj.tz:
                return obj
            else:
                return pd.Timestamp(obj, tz=self.tz, **kwargs)
        elif isinstance(obj, str):
            return pd.Timestamp(obj, tz=self.tz, **kwargs)

    def _relative(self, obj: str, **kwargs):
        """
        相对时间转为时间戳
        :param obj: 相对时间字符串，'-3D:-H'
        :param kwargs: base,相对时间基准
        :return: 毫秒时间戳
        """
        # 输入模式判断
        if not any([re.fullmatch(i, obj) for i in self.allow_pattern]):
            raise ValueError(f'string pattern not supported,got {obj}\nallow pattern{self.allow_pattern}')
        else:
            # 相对时间基准(默认当前时间)
            base = self._absolute(kwargs.get('base')) if kwargs.get('base') else self.now
            # 添加分隔符
            obj = obj if ':' in obj else obj + ":"
            # 提取value
            offset_value, align_value = re.split(':', obj)
            # 增加偏移
            offset = self._add_offset(base, offset_value) if offset_value else base
            # 增加对齐
            align = self._add_align(offset, align_value) if align_value else offset
            return align

    @property
    def ts(self):
        """
        :return: pandas TimeStamp时间戳
        """
        # 1.输入为空
        if self.obj is None:
            ts = self.now
        # 2.输入为字符
        elif isinstance(self.obj, str):
            if re.findall('[a-zA-Z]', self.obj):  # 包含字母则为相对时间
                ts = self._relative(self.obj, **self.kwargs)
            else:  # 绝对时间
                ts = self._absolute(self.obj, **self.kwargs)
        # 3.输入为数值或pd.TimeStamp
        else:
            # 绝对时间
            ts = self._absolute(self.obj, **self.kwargs)
        return ts

    @property
    def ms(self):
        """
        :return: 毫秒
        """
        return int(self.ts.timestamp() * 1e3)


def parallel_map(func, *iterables, thread: bool = False, **kwargs) -> list:
    """
    map函数的并行计算版本

    :param func: 并行函数
    :param iterables: func的位置参数
    :param thread: 是否为多线程
    :param kwargs: func的关键字参数
    :return: 与位置参数等长的列表
    """

    # 冻结位置参数
    p_func = partial(func, **kwargs)
    # 打开进程/线程池
    pool = ThreadPool() if thread else ProcessPool()
    try:
        start = time.time()
        # imap方法
        with tqdm(total=len(iterables[0]), desc="进度") as t:  # 进度条设置
            r = []
            for i in pool.imap(p_func, *iterables):
                r.append(i)
                t.set_postfix({'函数': func.__name__, "用时": f"{time.time() - start:.0f}秒"})
                t.update()
        return r
    except Exception as e:
        print(e)
    finally:
        # 关闭池
        pool.close()  # close the pool to any new jobs
        pool.join()  # cleanup the closed worker processes
        pool.clear()  # Remove server with matching state


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    if 'window' in platform.platform().lower():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip
    else:
        net_card = ['ens32', 'eth0', 'eno1']
        addr = 'localhost'
        for i in net_card:
            try:
                r = netifaces.ifaddresses(i)[netifaces.AF_INET]
                addr = r[0].get('addr')
            except:
                continue
        return addr


if __name__ == '__main__':
    print(get_host_ip())
