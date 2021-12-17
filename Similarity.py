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
def cosine_similarity(x,y):
    zeros = np.zeros(len(x))
    if len(x) == len(y):
        if (x == zeros).all() or (y == zeros).all():
            return float(1) if (x == y).all() == 0  else float(0)
        else:
            element = np.dot(x,y)
            denominator = (np.dot(x,x) * np.dot(y,y)) **0.5
            if denominator!= 0:
                result = element / denominator
                return result
            else:
                return "无法计算"
    else:
        return "长度不相等"

# 注：匹配系数需要去重; 并且适用于文本&数字
# 计算SMC 简单匹配系数
def SMC(x,y):
    # 取交集,交集的长度是m11
    #　全部　是lenx + leny
    a = [item for item in x if item in y]
    return len(a)/(len(x) + len(y))
# 计算Jaccard系数
def jaccard(x,y):
    # 取交集,交集的长度是m11
    #　分母　是lenx + leny - lena
    a = [item for item in x if item in y]
    return len(a)/(len(x) + len(y) - len(a))



if __name__ =="__main__":
    print(cosine_similarity(a,b))
    print(cosine_similarity(c,c))
    print(cosine_similarity(c,b))
    print(cosine_similarity(a,a))
    print(jaccard('abc','apple'))