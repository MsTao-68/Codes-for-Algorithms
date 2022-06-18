# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao
# Date: 2021/12/20
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
import operator
from operator import itemgetter
def clf(test, dataset, labels, k):
    datasetSize = dataset.shape[0] # 获取样本容量
    diff = np.tile(test, (datasetSize,1)) - dataset
    # 将测试数据增厚（len，1）与训练集相减，求与每一个点的距离
    # Andrew NG在deep learning 说 python 有广播机制（broadcasting），所以可以直接相减
    dist = ((diff**2).sum(axis =1))**0.5 # 求lp距离，axis=1表示按行相加
    sortedDist = dist.argsort() # 按照索引升序排序，用于索引label
#     print(sortedDist)
    count = {}
    for i in range(k):
        label = labels[sortedDist[i]]
        count[label] = count.get(label,0) + 1
    sortedCount = sorted(count.items(), key = operator.itemgetter(1),reverse= True)
    return sortedCount[0][0] # 返回最大的类别的键
def LoadData():
    data = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
    label =['爱情片','爱情片','爱情片','动作片','动作片','动作片','未知']
    return data,label

if __name__ == "__main__":
    data, labels = LoadData()
    testData = [18, 90]
    label = clf(testData, data, labels, 3)
    print(label)