# !usr\bin\python
# encoding: utf-8
# Author: Tracy Tao
# Date: 2021/12/19
from math import log
from operator import itemgetter
# calculate entropy
# H(D) = -sum(pi*log(pi))
def entropy(dataset):
    # 根据类的个数计算D的熵
    nCase = len(dataset) # 样本容量
    catlog = {} # 对不同类计数
    ent = 0.0 # 初始化熵
    for item in dataset:
        cat = item[-1] # 获取类名
        catlog[str(cat)] = catlog.get(str(cat),0) + 1
    for ci in catlog:
        pi = float(catlog[ci]) / nCase
        ent += -(pi * log(pi,2))
    return ent

# compute infomation gain
# Feature selection
def BestFeatureSelect(dataset, labels):
    Nfeature = len(labels) # 特征个数
    Ncase = len(dataset) # 样本容量
    Dentropy = entropy(dataset) # 计算经验上 H（D)
    maxGain = 0.0 # 初始化最大信息增益
    best = -1 # 记录索引
    # 计算所有信息增益 g(D,A) = H(D) - H(D,A)
    for i in range(Nfeature):
        # 获取A的值,去重frozenset
        vlist = [record[i] for record in dataset]
        Ai = frozenset(vlist)
        Aentro = 0.0 # 特征值的熵的初始化
        InfoGain = 0.0 # 初始信息增益
        for v in Ai:
            vcount = vlist.count(v)
            pv =  vcount / Ncase # 计算当前取值的概率
            Aentro += pv * entropy(vlist)
        InfoGain = Dentropy - Aentro # 计算信息增益
        #输出当前特征的信息增益
        print("第{}个特征{}的信息增益是{}".format(i + 1, labels[i], InfoGain))
        if(InfoGain > maxGain):
            maxGain = InfoGain
            best = i
        return maxGain,best

# 计算指定数据集的经验上
def Entropy(dataset):
    Nentries = len(dataset) # 返回样本容量
    Nlabels = {} # 记录标签出现次数
    Ent = 0.0 # 初试化经验熵
    for item in dataset:
        lbl = item[-1] # 获取类别名
        Nlabels[lbl] = Nlabels.get(lbl,0)+1
        # 如果存在就跟新计数，如果不存在就新建一个key
    for x in Nlabels:
        p = float(Nlabels[x]) / Nentries # 计算概率
        Ent += (-1) * log(p,2) # 经验熵公式
    return Ent

# 按照特征划分数据集
def SplitDataset(dataset, label, value):
    retDataset = [] # 返回的数据集
    for item in dataset:
        if item[label] == value:
            cut = item[:label]       #如果相等就去掉特征
            cut.extend(item[label+1:]) # 将符合条件的添加到返回的数据集
            retDataset.append(cut)
    return retDataset # 返回划分后的数据集

# 选择最优特征, 计算信息增益 = 经验熵 - 条件熵
def BestFeature(dataset):
    nFeature = len(dataset[0])- 1 # 根据第一条样本，去掉类别之后，计算特征数量
    Ent = Entropy(dataset) # 调用函数计算经验熵
    MaxInfoGain = 0.0 # 初始化最大信息增益
    BestIndex = -1 # 初始化最优特征的索引
    for i in range(nFeature): # 遍历索引所有特征
        FiValue = [item[i] for item in dataset] # 获取样本中所有该特征的取值
        UniqueValue = set(FiValue) # 去重，获得该特征值的集合
        ent = 0.0 # 初始化特征的经验熵
        for value in UniqueValue: # 遍历该特征的所有取值
            subset = SplitDataset(dataset, i, value) # 根据第i个特征的特征值划分数据集
#             print(subset)
            prob = float(len(subset)) / float(len(dataset)) # 计算子集的概率
            ent += prob * Entropy(subset) # 计算特征的 条件熵 H(D|A) = P（A） * H(A)
            InfoGain = Ent - ent # 计算信息增益
            print("第{}个特征的信息增益为{}".format(i,InfoGain))
            if InfoGain > MaxInfoGain:
                MaxInfoGain = InfoGain
                BestIndex = i
    return BestIndex # 返回信息增益最大的特征索引


# 统计类标签的情况 计算argmax(ci)
from operator import itemgetter
def ClassStats(classlist):
    Class ={} # 创建class字典统计类别出现的次数
    for x in classlist:
        Class[x] = Class.get(x,0) + 1 # 如果存在就更新次数，如果不存在就创建新的key
    sortedClass = sorted(Class.items(), key = itemgetter(1),reverse = True) # 根据值降序排列
    return sortedClass[0][0]


# 根据最优特征递归建决策树
def ID3 (dataset, labels, bestFeatureIndx):
    classList = [item[-1] for item in dataset]  # 获取类别列表
    if len(classList) <= 0:  # 如果不存在类别，直接退出
        return None
    if classList.count(classList[0]) == len(classList):  # 若只存在一个类别，直接返回类别
        return classList[0]
    if len(dataset[0]) == 1:  # 如果遍历完所有特征之后，直接返回最大的类别
        return ClassStats(classList)
    # 算法中三个独立考虑的标准判断完之后，正是建树
    bestF = BestFeature(dataset)  # 获得最优特征的索引
    bestL = labels[bestF]  # 获得最优特征的label
    bestFeatureIndx.append(bestL)
    myTree = {bestL: {}}  # 根据最优特征进行建树
    del (labels[bestF])  # 删除已经建树的特征
    Fvalues = [item[bestF] for item in dataset]  # 获得数据集中所有最优特征的值
    UniValue = set(Fvalues)
    for val in UniValue:
        subl = labels[:]  # 复制一份传入防止报错
        myTree[bestL][val] = ID3(SplitDataset(dataset, bestF, val), subl, bestFeatureIndx)
    print(bestFeatureIndx)
    return myTree

# 执行分类
def clf(inputTree, featureLbl, test): # 传入创建的树，类别，需要分类的样本
    if len(inputTree) != 0:
        T1 = next(iter(inputTree)) # 获取决策树结点
        T2 = inputTree[T1] # 获取子树
        featureIdx = featureLbl.index(T1) # 索引决策树结点
        for x in T2.keys():
            if test[featureIdx] == x: # 如果样本数据索引并匹配
                if type(T2[x]).__name__ == 'dict': # 如果子树仍然是树形结构，不是叶子结点
                    classLbl = clf(T2,featureLbl,test)
                else:
                    classLbl = T2[x]
                return classLbl # 返回分类结果


if __name__ =='__main__':
    dataSet = [[0, 0, 0, 0, 'no'],
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
    f = []
    myTree = ID3(dataSet, labels, f)
    # print(f)
    print(myTree)
    test = [0, 1,1]
    re = clf(myTree, f, test)
    print(re)


