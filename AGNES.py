# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021/12/22
import numpy as np
import operator
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
keys = ['average','complete','ward','single']

df = pd.read_csv('E:\\dasein_py\\Data Mining and Machine Learning\\Chapter9_KNN\\data\\ex1data1.txt')
dataset = np.array(df)

def distance(a,b):
    # 计算欧几里得距离
    return np.sqrt((a[0] - b[0])**2+(a[1] - b[1])**2)

# 聚类四距离
def Dmin(ci,cj):
    return np.min(distance(a,b) for a in ci for b in cj)
def Dmax(ci,cj):
    return np.max(distance(a,b) for a in ci for b in cj)
def Davg(ci,cj):
    return sum(distance(a,b) for a in ci for b in cj)/(len(ci) * len(cj))
def Dmean(ci,cj):
    return abs(sum(a for a in ci)/len(ci) - sum(b for b in cj)/len(cj))

# 注：算法效率很低，都是for循环，所以直接掉包实现
def find_min(M):
    x,y,fmin = 0,0,0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i!=j and M[i][j] < fmin:
                fmin = M[i][j]
                x,y = i,j
    return x,y,fmin

def AGNES(dataset, dist, k):
    c, M = [], [] # 初始化空列表，存放类和距离
    for i in dataset:
        ci=[]
        ci.append(i)
        c.append(ci)
    for i in c:
        Mi = []
        for j in c:
            Mi.append(dist(i,j))
            M.append(Mi)
    N = len(dataset)
    while N > k:
        x, y,fmin = find_min(M)
        c[x].extend(c[y])
        c.remove(c[y])
        m = []
        for i in c:
            mi =[]
            for j in c:
                mi.append(dist(i,j))
            m.append(mi)
        N-=1
    return c

def Agglomerative(dataset,keys):
    plt.figure(figsize=(20,20))
    for i in range(4):
        cluster = AgglomerativeClustering(linkage=keys[i], n_clusters=5)
        r = cluster.fit(dataset)
        print('聚类结果：',pd.Series(cluster.labels_).value_counts())
        plt.subplot(2,2,i+1)
        d0 = dataset[cluster.labels_ == 0]
        d1 = dataset[cluster.labels_ == 1]
        d2 = dataset[cluster.labels_ == 2]
        d3 = dataset[cluster.labels_ == 3]
        d4 = dataset[cluster.labels_ == 4]
        plt.plot(d0[:, 0], d0[:, 1], '*r',label = 0)
        plt.plot(d1[:, 0], d1[:, 1], '*b',label = 1)
        plt.plot(d2[:, 0], d2[:, 1], '*g',label = 2)
        plt.plot(d3[:, 0], d3[:, 1], '*k',label = 3)
        plt.plot(d4[:, 0], d4[:, 1], '*y',label = 4)
        plt.legend(loc='upper right')
    plt.show()


if __name__ == "__main__":
    Agglomerative(dataset,keys)