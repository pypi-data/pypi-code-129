# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 17:45
# @Author  : qxcnwu
# @FileName: create.py
# @Software: PyCharm

import os

import h5py
import numpy as np
import pandas as pd
from osgeo import gdal
from osgeo import osr
from tqdm import tqdm


def make_table(base_path: str):
    """
    记录该文件每个点经纬度
    Args:
        base_path: 文件路径
    Returns: 返回经纬度表格
    """

    # 获取行列号
    vh = os.path.basename(base_path).split(".")[2]
    h = vh[0:3]
    v = vh[3:]

    # 使用gdal.Warp对MODIS数据进行重投影。
    modis_lai = gdal.Open(base_path)
    subdataset_one = modis_lai.GetSubDatasets()[0][0]
    src_ds = gdal.Open(subdataset_one)
    adfGeoTransform = src_ds.GetGeoTransform()

    # 获取行数列数
    nXsize = src_ds.RasterXSize  # 列数
    nYsize = src_ds.RasterYSize  # 行数

    # 投影坐标系转换地理坐标系
    prosrs = osr.SpatialReference()
    prosrs.ImportFromWkt(src_ds.GetProjection())
    geosrs = prosrs.CloneGeogCS()
    ct = osr.CoordinateTransformation(prosrs, geosrs)

    # 存储经纬度
    datax = np.zeros((nXsize, nYsize))
    datay = np.zeros((nXsize, nYsize))
    for i in tqdm(range(nXsize)):
        for j in range(nYsize):
            px = adfGeoTransform[0] + i * adfGeoTransform[1] + j * adfGeoTransform[2]
            py = adfGeoTransform[3] + i * adfGeoTransform[4] + j * adfGeoTransform[5]
            col = ct.TransformPoint(px, py)
            datax[i][j] = col[0]
            datay[i][j] = col[1]

    return np.round(datax, 5), np.round(datay, 5), [h, v]


def save_hdf(npy_x: str, npy_y: str):
    meta = pd.read_csv("tmp.csv", header=None,index_col=None)
    datax = np.load(npy_x)
    datay = np.load(npy_y)
    for x, y, j in zip(datax, datay, meta.iloc[:,0]):
        f = h5py.File("meta/"+j+".hdf", "w")
        f.create_dataset("x", data=x.astype(np.float32), compression="gzip")
        f.create_dataset("y", data=y.astype(np.float32), compression="gzip")
        f.close()
    return


def main(base_dir: str):
    xList = []
    yList = []
    vh = []
    for file in os.listdir(base_dir):
        if file.split(".")[3] == "006":
            x, y, tmp = make_table(os.path.join(base_dir, file))
            xList.append(x)
            yList.append(y)
            vh.append(tmp)
    return xList, yList, vh


if __name__ == '__main__':
    save_hdf("x.npy", "y.npy")
    print("done")
