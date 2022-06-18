# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021\12\17

from math import *
import numpy as np
import pandas as pd

a = np.array([1, 2, 2, 1, 1, 1, 0])
b = np.array([1, 2, 2, 1, 1, 2, 1])
c = np.zeros(6)
# 余弦相似度，注：只能传入数组

# sample standard deviation 样本标准差
# 适用数组
def ssd(df):
    if len(df) > 1:
        return sqrt(sum((df - df.mean())**2)/(len(df) - 1))
    else:
        return "输入有误"
# 协方差
def covariance(x,y):
    if len(x) == len(y) and len(x) > 1:
        return (sum((x - x.mean()) * (y - y.mean())))/(len(x)-1)
    else:
        return "长度不等或者输入有误"

#皮尔逊相关系数 = sxy/(sx*sy) [-1,1]
def Pearson(x,y):
    if ssd(x) == 0 or ssd(y) == 0:
        return "error"
    else:
        return covariance(x,y)/(ssd(x) * ssd(y))

if __name__ == "__main__":
    print("样本标准差：",ssd(a),',标准差:',a.std(),',方差：', np.var(a))
    print(covariance(a,c))
    print(covariance(a,b))
    print(Pearson(a,c))
    print(Pearson(a,b))
    print(Pearson(a,a))
    print('np.cov:',np.cov(a,b))