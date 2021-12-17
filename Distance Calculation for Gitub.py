# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021\12\17

from math import *
import numpy as np
import pandas as pd




# 归一化 = 中心化 + 标准化，return u = 0 ,sd = 1
def normalization(df):
    df = (df - df.mean())/df.std()
    return df

# 注：所有距离都是计算共有部分
# 曼哈顿距离 你维向量 p=1
def manhattan(x,y):
    d = (sum(abs(xi - yi) for xi,yi in zip(x,y)))
    return d
# 欧式距离 n维向量 p=2
def euclidean(x, y):
    d = (sum((xi - yi)**2 for xi,yi in zip(x,y)))**0.5
    return d

# 闵可夫斯基距离是推广，含有一个参数相当于 p为参数
def Minkowski(x,y,p):
    d = (sum(abs(xi - yi)**p for xi,yi in zip(x,y)))**(1/p)
    return d

# 对比np生成数组的不同
arr1 = np.arange(1,5)
arr2 = np.random.rand(5)
arr3 = np.random.rand(1,5)
# Andrew ng 的deep learning中强调了用random.rand(1,5) 以区分行向量和列向量
arr4 = np.random.rand(5,1)
arr5 = np.zeros(5)
df1 = pd.DataFrame(arr3 * arr4)



if __name__ =="__main__" :
    print('对比三种不同矩阵相乘方式：')
    print(arr3.T * arr4)
    print(arr3 * arr4.T)
    print(arr3 * arr4)
    print("----------------------------------")
    print("归一化函数使用于矩阵或者数组：")
    print(normalization(arr3 * arr4))
    print(normalization(arr3))
    print("归一化函数使用于数据框：")
    print(normalization(df1))
    print("----------------------------------")
    print("欧式距离用于list，得到标量：")
    print(euclidean([1,2,3], [4,5,6]))
    print("欧式距离用于数组，得到数组：")
    print(euclidean(arr3, normalization(arr3)))
    print("欧式距离用于数组，得到标量：")
    print(euclidean(df1, df1.T))
    print('Minkowski & 欧式距离：')
    print(Minkowski(arr3, normalization(arr3),2), euclidean(arr3, normalization(arr3)))



