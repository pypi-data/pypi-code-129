#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2022/3/9 13:09
@Author   : ji hao ran
@File     : rtdb.py
@Project  : pkgDev
@Software : PyCharm
"""

import pandas as pd
from typing import List
from .data_source import Mysql
from functools import reduce

"""
rtdb-v10 标准实时库相关操作
"""
__all__ = ['RTDBPointTable', ]


class RTDBPointTable:
    """
    RTDB_V10 点位表
    """

    def __init__(self, rtdb: List[str] = None, project: List[str] = None):
        """

        :param rtdb: 实时库信息，host:db_name,如240:xxx
        :param project: 项目信息，host:db_name
        """
        self.rtdb = rtdb if rtdb is not None else ['234:jet_rtdb_v10_prod_4_hongbo', '240:jet_rtdb_v10_prod_4_hongbo']
        self.project = project if project is not None else ['244:jet_101_shzg_dev', '244:jet_101_jet_dev']

    @staticmethod
    def _one_rtdb_table(host, name):
        """一个实时库表"""
        # 实时库连接
        rtdb_con = Mysql(host=host, name=name)
        # 实时库系列表
        tb_tenant, tb_project, tb_meter, tb_point = rtdb_con.read(["tb_tenant", "tb_project", "tb_meter", "tb_point"])
        # 实时库表选择列
        tenant = tb_tenant[['tenant_id', 'tenant_name']]
        project = tb_project[['tenant_id', 'project_id', 'project_name']]
        meter = tb_meter[['tenant_id', 'project_id', 'meter_id', 'meter_name']]
        point = tb_point[['tenant_id', 'project_id', 'meter_id', 'point_id', 'point_name']]
        # 合并
        df = reduce(lambda x, y: pd.merge(x, y, how='left'), [point, meter, project, tenant])
        return df

    @staticmethod
    def _one_project_table(host, name):
        """单个项目表"""
        con = Mysql(host=host, name=name)
        # 项目系列表
        tb_equip, tb_sys_type, tb_equip_type = con.read(["tb_equip", "tb_sys_equip_sys_type", "tb_sys_equip_type"])
        # 项目表选择列
        tb_equip_col = [
            'site_id', 'equip_sys_type_id', 'equip_sys_id', 'equip_id', 'equip_name', 'equip_type',
            'template_id', 'rtdb_meter_id',
        ]
        equip = tb_equip[tb_equip_col].rename(
            columns={
                'site_id': 'project_id',
                'rtdb_meter_id': 'meter_id'
            }
        )
        sys_type = tb_sys_type[['equip_sys_type_id', 'equip_sys_type_name']]
        equip_type = tb_equip_type[['equip_type_id', 'equip_type_name']].rename(columns={'equip_type_id': 'equip_type'})
        df = reduce(lambda x, y: pd.merge(x, y, how='left'), [equip, sys_type, equip_type])
        return df

    @staticmethod
    def _concat(x: list, func):
        """合并所有项目表"""
        # 所有项目
        result = []
        for i in x:
            arg = i.split(':')
            arg[0] = f'192.168.1.{arg[0]}'
            result.append(func(*arg))
        df = pd.concat(result).drop_duplicates().reset_index(drop=True)
        return df

    @property
    def rtdb_table(self):
        return self._concat(self.rtdb, self._one_rtdb_table)

    @property
    def project_table(self):
        return self._concat(self.project, self._one_project_table)

    @property
    def pt(self):
        """点位表"""
        df = pd.merge(self.rtdb_table, self.project_table, how='left')
        # 填充缺失值
        df = df.fillna('null')
        # 增加点位id和点位名列
        id_col = ['tenant_id', 'project_id', 'meter_id', 'point_id']
        df['rtdb_id'] = df[id_col].apply(lambda x: '.'.join(x), axis=1)
        name_col = ['tenant_name', 'project_name', 'meter_name', 'point_name']
        df['rtdb_name'] = df[name_col].apply(lambda x: '.'.join(x), axis=1)
        # return
        return df
