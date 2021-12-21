# Codes-for-Algorithms
- Codes for realizing theories learned from Data Mining, Machine Learning, Deep Learning without using the present Python packages. (Just basic coding test to challenge myself).
- **Upload on a random basis.**

--------

1. Junior Data Processing
  - Calculate Distance **N dimensional vector**:
    - [x] euclidean
    - [x] manhattan
    - [x] Minkowski
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
    - Features:
      1. with **Square Loss Function**
      2. Fit for Simple Linear Regression &　Multi-variate Regression
      4. Plot Loss Function & Compare Yhat and YReal

    - [ ] Mini Batch Gradient Descent Regression **Working on Progress** 🦾
  - Classification
    - Decision Tree 
     - [x] Entropy: Compute the uncertainty of DateSet 
     - [ ] Information Gain
     - [ ] Decision Tree Visualization **Working on Progress** 🦾
     - [x] ID3 
     - [ ] C4.5 **Working on Progress** 🦾
    - Bayes
     - [ ] Naive Bayes **Working on Progress** 🦾
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
#### <div align="center"><font color='#00338D'>“我无坚不摧 将情藏得隐晦 只有那明月 知道过程壮烈”</font></div> 
    - [ ] KMeans
    - [x] Apriori
    - [x] FPGrowth  
  - Neural Network **Working on Progress** 👻👻👻👻

---
- **Hope that there's 0.1% possibility that I could start my journey to Computer Vision.**
  - By Tracy Tao (Dasein), a STEM GIRL in business world.
---
Post Scrpits:
- By the way, I wanna shout out loud that I love Elon Musk! 🧠

    
