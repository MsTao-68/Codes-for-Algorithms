# !usr/bin/python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021/12/01

# - 支持度：min_Sup = na / N
# - 置信度：min_conf = nab / na
# - sup >= min_Sip && conf >= min_cof
# 1. 非频繁项集的超集必然不是频繁项集。
# 2. 频繁项集的候选集是频繁项集

# 流程
# 第一次扫描数据库获取候选集（1-频繁项集）。并cut非频繁项集。
# 第二次扫描1-频繁项集找出1-频繁项集的2-候选集（2-频繁项集）。并cut非频繁项集。
# 第三次扫描2-频繁项集找出2-频繁项集的3-候选集。并cut非频繁项集。
# 如此继续，扫描k-频繁项集是就找出（k-1）-频繁项集的k-候选集。并cut非频繁项集。若（k-2）的前缀相同就归为一类。
# Q:为什么是k-2？
# A:因为k-候选集是这一轮生成的，所以cut未区分出k-频繁项集，由于（k-1）-频繁项集已经有了，合并两个k-1需要判断前k-2个是否相同。
# Stop @只剩1个或者0个项集。

# 根据公式，需要设置计数器计算支持度，所以是创建dict
def Round1 (dataset):
    # 由于初始化，所以单独设置扫描函数。
    c1 = []
    # 存放1频繁项集，数字表示项集元素个数
    for item in dataset:
        for x in item:
            if list(x) not in c1:
                c1.append(list(x))
    c1.sort()
    return c1


def get_freq_set (dataset, ci, min_support):
    # 参数为：原数据集，i频繁项集，最小支持度
    # 该函数功能：1.获取i候选集；2.判断是否是频繁项集：更新计数。
    # 1->2 ，所以需要存放所有支持度的dict作为剪枝依据。
    Freq = []  # 存放频繁项集
    sup_datak = {}  # 存放频繁项集的支持度
    all_support = dict()
    for item in ci:
        for x in dataset:
            if set(x).issubset(set(item)):
                # 判断是否是子集，如果是计数++，如果不是就开辟新的
                all_support[frozenset(x)] = all_support.get(frozenset(x), 0) + 1
    #     print(all_support)
    for i in all_support:
        if all_support[i] >= min_support:
            Freq.append(list(i))
            sup_datak[i] = all_support[i]
    #     print(Freq)
    return Freq, sup_datak


def get_ck (Freq, k):
    ck = []
    for i in range(len(Freq)):  # 用位置来索引元素
        for j in range(i + 1, len(Freq)):  # 第k次扫描是用来获取k-1项集，因此前缀是k-2
            l1 = list(Freq[i])[:k - 2]
            l2 = list(Freq[j])[:k - 2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                if k > 2:
                    new = list(set(Freq[i]) ^ set(Freq[j]))
                    # 因为频繁项集的子集也是频繁项集
                else:
                    new = set()
                for x in Fk:
                    if set(new).issubset(set(x)) and list(
                            set(Fk[i]) | set(Fk[j])) not in ck:  # 减枝 new是 x 的子集，并且 还没有加入 ck 中
                        ck.append(list(set(Fk[i]) | set(Fk[j])))
    return ck


# 主程序
def apriori (dataset, min_sup=.1):
    c1 = Round1(dataset)
    #     print(c1)
    f1, sup1 = get_freq_set(dataset, c1, min_sup)
    #     print(f1,sup1)
    F = [f1]  # 存放所有频繁项集
    #     print(F)
    sup = sup1  # 储存所有频繁项集的支持度
    k = 2
    while (len(F) > 2 and len(F[k - 2]) > 1):
        ck = get_ck(F[k - 2], k)
        fk, supk = get_freq_set(dataset, ck, min_sup)
        F.append(fk)
        sup.update(supk)
        k += 1
    if (0 <= len(F) <= 2):
        return f1, sup1
    else:
        return F, sup


if __name__ == '__main__':
    dataset = [['1', '2'], ['1'], ['2'], ['1', '3'], ['1', '3', '4'], ['2', '3', '5'],
               ['1', '2', '3', '5'], ['2', '5']]
    print(apriori(dataset))
