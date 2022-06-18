# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao
# Date: 2021/12/18

from math import log
import pandas as pd
import numpy as np


def createDataSet():
    dataSet=[[0, 0, 0, 0, 'no'],
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']]
    # 特征名称
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    return dataSet, labels

# calculate entropy
# H(D) = -sum(pi*log(pi))
def entropy(dataset):
    # 根据类的个数计算D的熵
    nCase = len(dataset) # 样本容量
    catlog = {} # 对不同类计数
    ent = 0.0 # 初始化熵
    for item in dataset:
        cat = item[-1] # 获取类名
        catlog[cat] = catlog.get(cat,0) + 1
    for ci in catlog:
        pi = float(catlog[ci]) / nCase
        ent += -(pi * log(pi,2))
    return ent

if __name__ == "__main__":
    dataset, lbl = createDataSet()
    print(entropy(dataset))

