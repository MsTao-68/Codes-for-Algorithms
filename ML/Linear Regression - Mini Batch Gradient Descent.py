# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2022/03/04

# %matplotlib inline
import random
import warnings
warnings.filterwarnings('ignore')
import torch
from d2l import torch as d2l


def synthetic_data(w, b, num_examples):  # @save
    '''
    params: w 权重
    params: b 偏置
    params: num_examples 样本量
    returns: ...
    '''
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))


def data_iter(batch_size, features, labels):
    '''
    params: batch_size 批量大小
    params: features 特征维数
    params: labels 标签属性
    returns: ...
    '''
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])  # 根据batch_size来切分样本
        yield features[batch_indices], labels[batch_indices]


def linreg(X, w, b):  # @save
    '''
    params: X样本数据集，
    params: w权重
    parmas: b偏置
    function: 单层单层神经网络模型
    returns: ...
    '''
    return torch.matmul(X, w) + b


def SquareLoss(yhat, y):
    '''
    parmas: yhat 预测的label
    parmas；y 真实的label
    function: 定义平方损失函数
    returns: 平方损失
    '''
    return (yhat - y.reshape(yhat.shape)) ** 2 / 2


def MSELoss(yhat, y):
    from torch.nn import MSELoss
    '''
    parmas: yhat 预测的label
    parmas；y 真实的label
    function: 定义均方损失函数
    returns: 均方损失
    '''
    return torch.nn.MSELoss(reduction='mean')(yhat, y)


def sgd(params, lr, batch_size):  # @save
    '''
    params: params X的值
    params: lr learning rate 学习率
    params: batch_size 批量大小
    '''
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size  # 更新param：[w,b]的值
            param.grad.zero_()


def main(params, lr, batch_size, num_epochs, loss_function, net, features, labels, w, b):
    '''
    params: params X的值
    params: lr learning rate 学习率
    params: batch_size 批量大小
    params: num_epochs 训练次数
    params: loss_function 损失函数
    params：net 模型调用
    params: batch_size 批量大小
    params: features 特征维数
    params: labels 标签属性
    params: w weight
    params: b bias
    returns: None
    '''
    for epoch in range(num_epochs):  # 循环epoch次
        for X, y in data_iter(batch_size, features, labels):  # 对生成数据计算损失
            l = loss_function(net(X, w, b), y)
            l.sum().backward()
            sgd([w, b], lr, batch_size)  # 调用随机梯度下降函数更新【w，b】的值
        with torch.no_grad():
            train_l = loss_function(net(features, w, b), labels)
            print(f'epoch: {epoch + 1}, lr: {lr}, loss: {float(train_l.mean()):.5f}')  # 对一个batch输出平均损失


if __name__ == "__main__":
    true_w = torch.tensor([2, -3.4])
    true_b = 4.2
    num_examples = 1000
    net = linreg
    loss = SquareLoss
    # 初始化模型参数
    w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)
    features, labels = synthetic_data(true_w, true_b, num_examples)  # 生成数据集
    for lr in [0.01, 0.03, 0.1]:
        main([w, b], lr, 10, 10, SquareLoss, net, features, labels, w, b)