# -*- coding: utf-8 -*-
# @Time    : 2022/8/11 22:09
# @Author  : qxcnwu
# @FileName: FoundPos.py
# @Software: PyCharm

import os
from typing import List

import h5py
import numpy as np
import pandas as pd


class Point:
    def __init__(self, name: str, x: int, y: int, distance: float, oldx: int, oldy: int, lon: float, lat: float):
        """
        Args:
            name: 第几副图像
            x: 行号
            y: 列号
            distance: 偏差单位度平方
            oldx: 图上经度
            oldy: 图上纬度
            lon: 查询经度
            lat: 查询纬度
        """
        self.hv = name
        self.row = x
        self.col = y
        self.distance = distance
        self.piclon = oldx
        self.piclat = oldy
        self.lon = lon
        self.lat = lat

    def __str__(self):
        return "图幅编号:" + self.hv + "\n图上行号:" + str(self.row) + "\n图上列号:" + str(self.col) + "\n实际误差:" + str(
            self.distance) + "\n图上经度:" + str(self.piclon) + "\n图上纬度:" + str(self.piclat) + "\n查询经度:" + str(
            self.lon) + "\n查询纬度:" + str(self.lat)


class FD:
    def __init__(self, distance: float = 0.003391):
        """
        init class fd
        0.003391=0.00225+0.001141
        Args:
            distance:
        """
        self._abspath = os.path.split(os.path.abspath(__file__))[0]
        base_dir = os.path.join(self._abspath, "meta/tmp.csv")
        if not os.path.exists(base_dir):
            raise FileNotFoundError("no such meat data ", base_dir)
        self._metaData = pd.read_csv(base_dir, header=None, index_col=None)
        self._bound = np.array(self._metaData.iloc[:, 1:])
        self._hdf = {}
        self.distance = distance

    @classmethod
    def isContain(cls, path):
        """
        path contains
        Args:
            path:
        Returns:
        """
        return os.path.exists(path)

    def found(self, lon, lat):
        """
        查询单个经纬度坐标
        Args:
            lon:
            lat:
        Returns:
        """
        idx = np.where(np.logical_and(
            np.logical_and(lon <= self._bound[:, 1], lon >= self._bound[:, 0]),
            np.logical_and(lat <= self._bound[:, 3], lat >= self._bound[:, 2])
        ))
        if len(idx) == 0:
            return None
        answer = []
        for id in idx[0]:
            tmp = self.__found(lon, lat, id)
            if tmp.distance > self.distance:
                continue
            answer.append(tmp)
        return answer

    def __found(self, lon, lat, idx):
        """
        顺序查找
        Args:
            lon:
            lat:
            idx:
        Returns:
        """
        hv = self._metaData.loc[idx, 0]
        path = os.path.join(self._abspath, "meta", hv + ".hdf")
        if self._hdf.__contains__(hv):
            tmpx = self._hdf.get(hv)[0]
            tmpy = self._hdf.get(hv)[1]
        else:
            if not self.isContain(path):
                raise FileNotFoundError("No such file ", path)
            tmp = h5py.File(path, 'r')
            tmpx = np.array(tmp.get("x"))
            tmpy = np.array(tmp.get("y"))
            self._hdf.update({
                hv: [tmpx, tmpy]
            })
        tp = np.abs(tmpx - lon) + np.abs(tmpy - lat)
        c = np.argmin(tp)
        x, y = c // 2400, c % 2400
        return Point(hv, x, y, np.min(tp), tmpx[x, y], tmpy[x, y], lon, lat)

    def founds(self, points: List[List[float]]):
        """
        查找多个点
        Args:
            points:
        Returns:
        """
        answer = []
        for point in points:
            answer.append(self.found(point[0], point[1]))
        return answer


if __name__ == '__main__':
    # 初始化查询对象
    fd = FD()
    # 查询单个点
    answer = fd.found(115, 33)
    # 查询多个点
    answers = fd.founds([[115, 33],[105, 43],[99, 47.12]])
    # 查看结果
    ans=answer[0]
    print(ans)