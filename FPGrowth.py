# !usr/bin/python
# encoding: utf-8
# Author: Tracy Tao (Dasein)
# Date: 2021/12/01

# 算法流程以及思路
#1.  Create Tree
#   第一次扫描dataset，计数
#   设定min_support
#   sort（）and delete < min_support的item
#   重新调整清单
# 2. 扫描新的dataset，Create FP Tree
#   Add（）并更新计数
# 3. 挖掘频繁项集
# 4. 获取对应条件模式基

# 创建树类
class TreeNode:
    def __init__(self, name, Occur, Parent):
        self.name = name    # 节点名称
        self.Occur = Occur  # 记录出现的次数
        self.Parent = Parent    #父节点
        self.link = None    # 用于存放相似Elem的地址
        self.child = {}     # 存放子节点
    def increase(self, Occur):
        self.Occur += Occur # # 对出现次数进行计数
    def display(self, idx = 1):
        print(' '*idx, self.name, self.Occur) # FP增长树可视化
        for x in self.child.values():
            x.display(idx + 1)

def Create(dataset, minSup = 1):    # Create Tree
    Head = {} # 创建空头节点
    for item in dataset: # 第一次扫描数据集
        for x in item:
            Head[x] = Head.get(x, 0)+ dataset[item]
    HeadTable = {k:v for k,v in Head.items() if v >= minSup}
    # print(Head)
    freq = set(HeadTable.keys())
    # print('freqItemSet:', freq)
    if len(freq) == 0:
        return None, None # 若无元素，则直接return退出
    for x in HeadTable:
        HeadTable[x] = [HeadTable[x], None] # 初始化head
#     print('HeadTable', Head)
    # 第二次扫描dataset
    retTree = TreeNode('NUll', 1, None) # 创建根节点
    for item, Occur in HeadTable.items():
        temp = {}
        for x in item: # put transaction items in order
            if x in freq:
                temp[x] = HeadTable[x][0]
        if len(temp) > 0:
            ordered = [item[0] for item in sorted(temp.items(), key= lambda x: x[1],reverse= True)]
            updTree(ordered, retTree, HeadTable, Occur)  # 将排序后顺序去更新数
    return retTree, Head # 返回数和头指正表

def updTree(ordered, inTree, HeadTable, Occur):
    # 检查是否第一个元素是否以子节点方式存在, 如果是就计数+1，并更新计数
    if ordered[0] in HeadTable.child:
        inTree.child[ordered[0]].increase(Occur)
        # 如果存在，就更新头结点的计数
    else:
        # 如果不是子节点，就创建一个新的子节点，Create TreeNode
        inTree.child[ordered[0]] = TreeNode(ordered[0], Occur, inTree)    # retTree是新建Node的父节点
        if HeadTable[ordered[0]][1] == None:
            # 没有孩子就是空的，所以要存放刚才新建的Node作为孩子结点,因为创建了所以非空，不需要再判断是否为空
            HeadTable[ordered[0]][1] = HeadTable.child[ordered[0]]
        else:
            updHeader(HeadTable[ordered[0]][1], inTree.child[ordered[0]])   # 如果不是None，就更新Header
    if len(ordered) > 1: #如果有孩子结点，就遍历孩子结点，去更新刚才的计数
        # 自上而下的去更新树
        updTree(ordered[1::], inTree.child[ordered[0]], HeadTable, Occur)

def updHeader(NewNode, TargetNode):
    # 更新头指针表，并且使得每个节点存放的地址指向该节点实例化对象
    while NewNode.link != None:
        NewNode = NewNode.link # 使节点实例化对象指向节点
    NewNode.link = TargetNode # 更新指针域，指向目标节点

# 抽取条件模式基, 自下而上的遍历树，获取路径列表， # 用自下而上回溯，所以命名为上升树
def ascTree(LeafNode, prefix):
    if LeafNode.Parent != None:
            prefix.append(LeafNode.name)
            ascTree(LeafNode.Parent, prefix)

def findPrefix(patbase, Tnode):
    cpb ={}     # 条件模式基：Conditional Pattern Base
    while Tnode != None:
        #节点初始化过，（调用过TreeNode创建的就不是None）
        temp_prefix =[]     # 初始化空列表存放prefix
        ascTree(Tnode,temp_prefix)
        # 上溯整棵树，获取prefix（因为ascTree自己递归自己，所以肯定是遍历完了整棵树）
        if len(temp_prefix) > 1 :
            # 条件模式基不包括叶节点，所以>1才有意义，=1只有一个根节点（它自己又是叶子节点，是个paradox）
            cpb[frozenset(temp_prefix[1:])] = Tnode.count
        Tnode = Tnode.link
    return cpb

# 递归查找频繁项集
def mineTree(inTree, HeadTable, minSup, prefix, freqList):
    l = [v[0] for v in sorted(HeadTable.items(), key = lambda m:m[1][0], reverse= True)]    # 排序头指针
    for patbase in l:   # # 遍历排序过的头指针表，获取键值
        newFreqSet = prefix.copy()
        newFreqSet.add(patbase)     # 复制条件模式基，将其添加进新频繁项集，进行保存
        print('Final Freq Item:', newFreqSet)
        # 输出当前获得的新频繁项集
        freqList.append(newFreqSet)     # 将它保存进总的频繁项集
        Cpatbases = findPrefix(patbase, HeadTable[patbase][1])
        print('Conditional Pattern Base:', patbase, Cpatbases)
        myCondTree, myHead = Create(Cpatbases, minSup)      # 从条件模式基创建，条件FPtree
        print('Header:', myHead)
        if myHead != None:
            print('Conditional Tree FreqSet:', newFreqSet)
            # 挖掘条件FP树
            myCondTree.disp(1)
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqList)
            # 不断递归调用进行条件fp树的挖掘，
            # 第一个参数：要挖掘的树的更新
            # 第二个参数：传入头指针
            # minSup不变
            # 总的频繁项集，每次递归调用都会讲条件fp数条件模式基的频繁项集加入

def loadSimpDat():
    simpDat = [
                ['I1','I2','I5'],
                ['I2','I4'],
                ['I2','I3'],
                ['I1','I2','I4'],
                ['I1','I3'],
                ['I2','I3'],
                ['I1','I3'],
                ['I1','I2','I3','I5'],
                ['I1','I2','I3']
              ]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = retDict.get(frozenset(trans), 0) + 1 #若没有相同事项，则为1；若有相同事项，则加1
    return retDict

if __name__ == "__main__":
    minSup = 2
    simpDat = loadSimpDat()
    # print("Dataset:", simpDat)
    initSet = createInitSet(simpDat)
    # print('Initiated Dataset:', initSet)
    myFPtree, myHeaderTab = Create(initSet, minSup)
    print(myFPtree, myHeaderTab)
    myFPtree.display()
    myFreqList = []
    mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
