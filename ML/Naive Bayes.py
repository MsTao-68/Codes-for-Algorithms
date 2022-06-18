# !usr\bin\python\
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021/12/22
# 舆情监测（初级版）
'''
算法流程：
1. 计算每个类别的文档数目
    对每个类别，统计词出现的次数
    岁每个类别计算条件概率
2. 返回每个类别的条件概率
'''
import numpy as np

# 文本分类 - 偏好检测之判别正负面情绪语言,1：+，0：-
def loadDataset():
    posters=['Elon Musk is my idol',
            'Artificial Intelligence is a great bliss to this day and age',
            'Stop posting those stupid twitters',
            'You are stupid that you are wasting time']
    for i in range(len(posters)):
        posters[i] = posters[i].split()
    labels = [1,1,0,0]
    words=set([]) # 创建空集合，因为要去重
    for item in posters:
        words = words | set(item) # 获得并集
    return posters,labels, list(words)

def WordVec(wordsList, dataset): # 将原始文本数据转化为0-1，即1为存在于wordslist，0为不存在wordlist
    retVec = [0] * len(wordsList) # 创建类似独热编码的表，记录是否存在
    for x in dataset:
        if x in dataset:
            retVec[wordsList.index(x)] = 1 # 索引出现的位置，在返回的table中相应的位置更新数据
        else:
            print("{} is not in my WordList".format(x))
    return retVec

def processing(wordlist,dataset):
    training = []
    for i in dataset:
        training.append(WordVec(wordlist,i))
    return training

def NaiveByes1 (training, label):
    Ntraining = len(training)  # 样本容量
    Nwords = len(training[0])  # 单词数
    Npositive = np.zeros(Nwords)  # 统计积极性词汇的次数列表初始化
    Nnegative = np.zeros(Nwords)  # 统计负面词汇的次数列表初始化
    pn = sum(label) / float(len(training))  # 计算积极性文件先验概率
    P = 0.0  # 积极性词汇总数
    N = 0.0  # 负面词汇总数
    for i in range(Ntraining):  # 遍历训练数据
        if label[i] == 1:
            Npositive += training[i]
            P += sum(training[i])  # 如果是积极性文件，那么就在里面更新去重词汇表各个词汇出现的次数
        else:
            Nnegative += training[i]
            N += sum(training[i])
    p1 = Npositive / P
    p0 = Nnegative / N  # 计算每个类别下的条件概率
    return p0, p1, pn

# 利用拉普拉斯平滑，因为数据量小，0元素会过多影响结果
def NaiveByes2(training, label):
    Ntraining = len(training) # 样本容量
    Nwords = len(training[0]) # 单词数
    Npositive = np.ones(Nwords) # 统计积极性词汇的次数列表初始化
    Nnegative = np.ones(Nwords) # 统计负面词汇的次数列表初始化
    pn = sum(label) / float(len(training)) # 计算积极性文件先验概率
    P = 2.0 # 积极性词汇总数
    N = 2.0 # 负面词汇总数
    for i in range(Ntraining): # 遍历训练数据
        if label[i] == 1:
            Npositive += training[i]
            P += sum(training[i]) # 如果是积极性文件，那么就在里面更新去重词汇表各个词汇出现的次数
        else:
            Nnegative += training[i]
            N += sum(training[i])
    p1 = Npositive / P
    p0 = Nnegative / N # 计算每个类别下的条件概率
    return p0, p1, pn

# 利用拉普拉斯平滑，和对数处理结果,增大数值
def NaiveByes3(training, label):
    Ntraining = len(training) # 样本容量
    Nwords = len(training[0]) # 单词数
    Npositive = np.ones(Nwords) # 统计积极性词汇的次数列表初始化
    Nnegative = np.ones(Nwords) # 统计负面词汇的次数列表初始化
    pn = sum(label) / float(len(training)) # 计算积极性文件先验概率
    P = 2.0 # 积极性词汇总数
    N = 2.0 # 负面词汇总数
    for i in range(Ntraining): # 遍历训练数据
        if label[i] == 1:
            Npositive += training[i]
            P += sum(training[i]) # 如果是积极性文件，那么就在里面更新去重词汇表各个词汇出现的次数
        else:
            Nnegative += training[i]
            N += sum(training[i])
    p1 = np.log(Npositive / P)
    p0 = np.log(Nnegative / N) # 计算每个类别下的条件概率
    return p0, p1, pn

def clf_nb(testVec, p0, p1, pn):
    # 公式 p(c|w) = p(w|c) *p(c) / p(w)
    # 朴素贝叶斯条件独立性假设： p(w|c) = p(w1,w2,...|c) = p(w1|c) * ...p(wn|c)
    # 拉普拉斯平滑版，并且取了对数所以是加法
    P1 = sum(testVec * p1) + np.log(pn)
    P0 = sum(testVec * p0) + np.log(1-pn)
    if P1 > P0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    data, labels, wordList = loadDataset()
    training = processing(wordList, data)
    p0, p1, pn = NaiveByes3(training, labels)
    test = ['Elon', 'Musk', 'is', 'bliss']
    testvec = WordVec(wordList,test)
    print('初级舆情分类结果：', clf_nb(testvec,p0,p1,pn))
    print('----------------------------------------------')

