# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021\12\17

import pandas as pd
import numpy as np
import random
from random import random
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
sns.set(style='darkgrid',font_scale=1.2)
plt.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False
true_theta = np.array([4.2, 3, 5,1,2])
# 定义线性回归模型，根据公式矩阵乘法
def H(X, theta):
    return np.dot(X,theta)
# 定义平方损失函数
def SquareLoss(yhat, y):
    return np.sum(np.power((yhat - y),2))/(2 * len(y))
# 定义 0-1 损失函数
def ZeroOneLoss(yhat, y):
    if yhat != y:
        return 1
    else:
        return 0
# 定义绝对损失函数
def QuadraLoss(yhat,y):
    return np.sum(np.abs(yhat - y))
# 定义对数损失函数
def LogLoss(yhat, y, eps = 1e-15):
    import numpy as np
    yhat = np.array(yhat)
    y = np.array(y)
    assert (len(yhat) and len(y) == len(yhat))
    # Clip yhat between eps & 1-eps
    p = np.clip(yhat, eps, 1-eps)
    return (np.sum(-y * np.log(p) - (1-y)*np.log(1-p))) / len(y)

# 定义批量梯度下降函数
def GradientDescent(X, y, theta, alpha, iters, loss_func):
    '''
    params:
    X - Training DataSet
    y - Training Values(Labels)
    theta - model parameters
    alpha - learning rate
    iters - epochs
    loss_func - function name
    returns:
    theta_hat
    '''
    temp = np.zeros(len(theta)) # 初试化temp，用于同时更新参数
    cost = np.zeros(iters)    # 初试化cost，用于记录每次训练的损失
    nParam = int(np.ravel(theta).shape[0])  # 展平参数，形成1维数组，统计参数个数
    for i in range(iters):      # 训练iters次，用for-循环
        error = H(X, theta) - y     # 矩阵运算计算误差
        # 对每个参数求偏导数，得到梯度
        for j in range(nParam):
            # 计算每个theta0,并且重塑成error的维度
            term =  error * X[:,j].reshape(error.shape)
            temp[j] = theta[j] - (alpha/len(X))*np.sum(term)
        # 同时更新所有参数
        theta = temp
        yhat2 = H(X, theta)
        if loss_func == 'SquareLoss':
            Loss = SquareLoss(yhat2, y)
        elif loss_func == 'ZeroOneLoss':
            Loss = ZeroOneLoss(yhat2, y)
        elif loss_func == 'QuadraLoss':
            Loss = QuadraLoss(yhat2, y)
        else:
            Loss = LogLoss(yhat2, y)
        cost[i] = Loss
        if (i+1) % 100 ==0:
            print("Epoch:{}, Loss:{}, theta:{}, LossFunc:{}".format(i, Loss, theta, loss_func))
            plot(cost,X,theta)
    return theta
# 定义模函数
def real_func(X,true_theta):
    return np.dot(X,true_theta)
# 绘制损失函数图
def plot(cost, X ,theta):
    plt.figure(figsize=(20,10))
    xs = list(range(len(cost)))
    plt.subplot(1,2,1)
    plt.plot(xs,cost,'-r',label="Training")
    plt.title("Training Loss")
    plt.subplot(1,2,2)
    plt.plot(X[:,1],H(X,theta),'*r', label = "Yhat")
    plt.plot(X[:,1],real_func(X,true_theta),"*g",label="Real")
    plt.title('vs')
    plt.legend()
    plt.show()

if __name__ =='__main__':
    X = np.random.rand(1000, 4)
    X = np.insert(X, 0, values=np.ones(1), axis=1)
    t = np.array([0, 0, 0, 0, 0])
    alpha = 0.01
    iters = 500
    print(GradientDescent(X, real_func(X, true_theta), t, alpha, iters,LogLoss))
