# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 16:15
# @Author  : qxcnwu
# @FileName: verification_hdf.py
# @Software: PyCharm

import os

import h5py
import numpy as np
import pandas as pd

clip=200
qq=2400//clip

index = np.array([i * clip for i in range(2400 // clip)])
xidx = np.zeros((2400 // clip, 2400 // clip),dtype=np.int_)
yidx = np.zeros((2400 // clip, 2400 // clip),dtype=np.int_)
for i in range(2400//clip):
    xidx[:,i]=index.T
    yidx[i]=index

def parse_one(hdf_path: str):
    """
    解析单独文件
    Args:
        hdf_path:
    Returns:
    """
    file = h5py.File(hdf_path, "r")
    x = np.array(file.get("x"))
    y = np.array(file.get("y"))
    x=x[xidx,yidx].reshape((qq*qq,1))
    y=y[xidx,yidx].reshape((qq*qq,1))
    return np.concatenate([x,y],axis=1)

def main(base:str):
    ans=[]
    for file in os.listdir(base):
        if not file.endswith("hdf"):
            continue
        path=os.path.join(base,file)
        ans.append(parse_one(path))
    return np.concatenate(ans)

if __name__ == '__main__':
    da=main("meta/")
    pd.DataFrame(da).to_csv("point.csv",header=False,index=False,index_label=False)