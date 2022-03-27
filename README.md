# Codes-for-Algorithms
- Codes for realizing theories learned from Data Mining, Machine Learning, Deep Learning without using the present Python packages. (Just basic coding test to challenge myself).
- **Upload on a random basis.**

--------

1. Junior Data Processing
  - Calculate Distance **N dimensional vector**:
    - [x] euclidean
    - [x] manhattan
    - [x] Minkowski
    - [x] Chebyshev
  - Calculate Similarity: 
    - [x] Jaccard
    - [x] Simple Matching Coefficent(SMC) 
  - Calculate relevance:
    - [x] Covariance
    - [x] Sample Standard Deviation (ssd)
    - [x] Pearson Coeffiencent 
2. Models
  - Linear
    - [x] Batch Gradient Descent Regression 
      - Batch Gradient Descent Regression Version 2.0 added @4 March, 2022 
        - Summary all loss function   
    - [ ] Mini Batch Gradient Descent Regression
      - [x] Linear Model - Mini Batch Gradient Descent Regresion using Pytorch  
    - Features:
      1. with **Square Loss Function**
      2. Fit for Simple Linear Regression &　Multi-variate Regression
      4. Plot Loss Function & Compare Yhat and YReal

    - [ ] Mini Batch Gradient Descent Regression **Working on Progress** 🦾
  - Classification
    - Decision Tree 
     - [x] Entropy: Compute the uncertainty of DateSet 
     - [ ] Information Gain
     - [ ] Decision Tree Visualization 
     - [x] ID3 
     - [ ] C4.5 **Working on Progress** 🦾
    - Bayes
     - [x] Naive Bayes
       - 对属性集和类变量的概率建模，**监督**学习
       - 假定一个属性对给定类的影响独立于其他属性的值，不存在依赖关系
       - 算法：
         - 利用贝叶斯公式计算每个类别的后验概率 P(Y=yi|X) = P(X|Y=yi)*P(Y=yi)/P(X)
         - 选择使得后验概率最大的类yi
         - 条件独立性：假设属性之间独立：P(X|Y=yi） = PI(P(X=xi|Y=yi))
            - P(Y=yi|X) = argmax{Y=Ci}(P(X|Y=yi)*P(Y=yi)/P(X))
         - 后验概率最大化，等价于期望风险最小化
            - 0-1损失 R（f）= E(L(Y,f(X))
            - 条件期望：R(f) = Ex(sum(L(yi,f))*P(yi|X))
            - 条件期望最小化，可以结合0-1损失函数转化为后验概率最大化原则
        - 方法
          - 极大似然估计
          - 贝叶斯估计
            1. 连续属性的类条件概率估计：将连续属性离散化，用相应的离散取件替换连续属性值，通过计算类与的训练记录中落入指定取件的比率来估计条件概率
            2. 二分划分：给新属性设置一个划分
            3. 概率密度估计：假定属性服从一个概率分布，利用训练数据估计分布的参数，确定分布之后利用分布估计类的条件概率
        - 算法流程
          1. 确定特征属性
          2. 获取训练集
          3. 对类别计算先验概率
          4. 对每个特征属性属性值计算所有划分的条件概率
          5. 用先验概率和条件概率计算后仰概率，将argmax作为类别输出
          -----
         - [x] 初级版舆情监测 
    - Sigmoid
     - [ ] Logistic Regression **Working on Progress** 🦾
  - Cluster
    - [x] K-Nearest Neighbor
        - K近邻算法
          - “物以类聚，人以群分”思想
          - “少数服从多数”思想
            - 若无法判定属于哪个类，就归为权重大的类
        - 要素
          1. 距离
          2. K值
            - K值选择
            1. If K值较小 then 距离很近才能进行预测，由于具有噪声，整体模型过于复杂，会发生过拟合现象
            2. IF K值较大 then 近似误差会较大，不相似点归为同一类，预测错误，模型过于简单
            3. If K = N，信息大量损失，模型过于简单
              - 用cross validation 来选择最优的k值
          3. 分类决策规则
          - 多数表决法
            - 注：计算距离时p值不同最邻近点会不同。
        - 算法原理
          - input: 带类标记的样本数据集合；没有标签的数据
          - process: 将型数据的每个特征与样本集的特征比较，提取前K个最相似的标签
          - output: 新分类结果
          1. 计算training中的点与当前点的距离
          2. 按距离递增排序
          3. 选取与当前点距离最小的k个点
          4. 统计前k个点中每一类的频率
          5. 返回频率最大的training中的点的类别
          6. 统计分类错误率
        - Tricks for Data Analysis
          - 输出分类结果之后，做分类错误率统计
          - 数据预处理-> 数据可视化：原始数据的分类结果
          - 用K近邻建模，计算错误率
          - 看错误率调整K值
            - K近邻受数值的影响较大，对数据进行归一化处理 new = (old - min)/(max - min)
            - train_test_split,检验准确率
            - 调整测试数据比例或者K来调参
    - [x] 层次聚类 AGNES
        - 自底向上: 自底向上合并组，计算组间相似度
        - input: dataset
        - output: clusters
          1. 将每个对象初始化成一个簇
          2. repeat
          3. 计算簇距离（矩阵运算），找到最相近的簇
          4. 合并相近簇成新簇
          5. until 停止条件K/D
        - 距离度量方法：最小距离；最大距离；均值距离；平均距离
        - 算法复杂度：O(n^2),空间复杂度：因为存放相似度矩阵
    ------
    - [ ] 层次聚类 DIANA 
    - [ ] KMeans
    - [x] Apriori
    - [x] FPGrowth  
  - Neural Network **Working on Progress** 👻👻👻👻
3. Optimization 最优化
- [x] Newton 插值
- [x] Lagrange 插值
- [ ] 精确线性搜索
- [ ] 非精确线性搜索
- [x] Wolf 算法

4. Deep Learning 深度学习
- [x] Softmax
- [x] MLP 多层感知机
- [ ] CNN Convolutional Nueral Network 卷积神经网络
- [ ] LSTM 长短记忆神经网络
- [ ] LSRM + Attention
- [ ] RNN 循环神经网络

5. OpenCV Computer Vision 计算机视觉与数字图像处理
- 待更新



#### <div align="center"><font color='#00338D'>“Grant me what the heart really wants.”</font></div> 
---
- **Hope that there's 0.1% possibility that I could start my journey to Artficial Intelligence.**
  - By Tracy Tao (Dasein), a STEM GIRL in business world.
---
Post Scrpits:
- By the way, I wanna shout out loud that I love Elon Musk! 🧠
- Grant is more brainy than Elon Musk. >.<
- 初心何见 清风拂心弦。
    
