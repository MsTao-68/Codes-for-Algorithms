# !usr/bin/python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2022/01/03


import numpy as np
from sympy import *
import re

'''
Wolfe-Powell非精确线性搜索，返回函数f在x处，方向d时的步长alpha
'''


def WolfePowell (f, d, x, alpha_, rho, sigma):
    maxk = 1000  # 迭代上限
    k = 0
    phi0 = fun(x)
    dimensions = dim(f_)

    dx = []
    grad = []
    for a in range(dimensions):
        dx.append(diff(f, symbols('x' + str(a), real=True)))  # 求偏导
        item = {}
        for i in range(dimensions):
            item[x_[i]] = x[i]
        grad.append(dx[a].subs(item))  # 求梯度

    phi0_ = np.dot(grad, d)
    print(dx)
    print(grad)

    a1 = 0
    a2 = alpha_
    alpha = (a1 + a2) / 2
    phi1 = phi0
    phi1_ = phi0_

    k = 0
    for k in range(maxk):  # 已设置迭代次数，使用有限次数迭代
        phi = fun(x + alpha * d)
        if phi <= phi1 + rho * alpha * phi1_:
            newx = x + alpha * d
            newdx = []
            newgrad = []
            for a in range(dimensions):
                newdx.append(diff(f, symbols('x' + str(a), real=True)))  # 求偏导
                newitem = {}
                for i in range(dimensions):
                    newitem[x_[i]] = newx[i]
                newgrad.append(newdx[a].subs(newitem))  # 求梯度

            phi_ = np.dot(newgrad, d)

            if phi_ >= sigma * phi0_:
                break
            else:
                alpha_new = alpha + (alpha - a1) * phi_ / (phi1_ - phi_)
                a1 = alpha
                alpha = alpha_new
                phi1 = phi
                phi1_ = phi_
        else:
            alpha_new = a1 + 0.5 * (a1 - alpha) ** 2 * phi1_ / ((phi1 - phi) - (a1 - alpha) * phi1_)
            a2 = alpha
            alpha = alpha_new
    k = k + 1
    return alpha


# 利用正则表达式，计算目标函数的维度


def dim (f_):
    dimension_set = []
    dimension_set = re.findall(r'x[0-9]\d*', str(f_))
    dimensions = len(set(dimension_set))
    return dimensions


x_ = []
for a in range(100):
    x_.append(symbols('x' + str(a), real=True))  # 设置符号变量


def fun (x_):
    return x_[0] ** 4 + x_[0] ** 2 + x_[1] ** 2  # 设置多项式目标函数，本例子设置的是三位高次方程


f_ = fun(x_)  # 用于W-P

alpha_ = 1
rho = 0.25  # rho 范围（0,1/2）
sigma = 0.5  # sigma 范围（rho，1）
x = np.array([1,1])  # 随机的初始点
d = np.array([-3, -1])  # 初始方向

alpha = WolfePowell(f_, d, x, alpha_, rho, sigma)
print(alpha)
