# OpenAI GPT2

- 它在文本生成上有着惊艳的表现，其生成的文本在上下文连贯性和情感表达上都超过了人们对目前阶段语言模型的预期。仅从模型架构而言，GPT-2 并没有特别新颖的架构，它和只带有解码器的 transformer 模型很像。

- **GPT-2 和语言建模**

  - **语言模型**

    简单说来，语言模型的作用就是根据已有句子的一部分，来预测下一个单词会是什么。最著名的语言模型你一定见过，就是我们手机上的输入法，它可以根据当前输入的内容智能推荐下一个词。从这个意义上说，我们可以说 GPT-2 基本上相当于输入法的单词联想功能，但它比你手机上安装的此类应用大得多，也更加复杂。OpenAI 的研究人员使用了一个从网络上爬取的 40GB 超大数据集「WebText」训练 GPT-2，该数据集也是他们的工作成果的一部分。

  - Transformer： all you need is attention / The Illustrated Transformer
  - 模型堆叠

- GPT-2 是使用「transformer 解码器模块」构建的，而 BERT 则是通过「transformer 编码器」模块构建的。

---

## 论文

- 摘要：我们证明，当对数百万个名为WebText的网页的新数据集进行训练时，**语言模型**开始学习这些任务而不需要任何明确的监督。语言模型的容量对于zero-shot任务迁移的成功至关重要，并且增加它可以跨任务以对数线性方式提高性能。我们最大型号的GPT-2是一个1.5B参数的Transformer，它在zero-shot设置中的8个测试语言建模数据集中的7个中实现了最先进的结果，但仍然不适合WebText。该系统学会从**自然发生的示范中完成任务**。
- 更通用的系统，它可以执行许多任务 - 最终无需为每个任务手动创建和标记训练数据集。
- 在本文中，我们将这两个工作线连接起来，并继续采用更一般的转移方法。我们演示语言模型可以在 zero-shot 设置中执行下游任务 - 无需任何参数或体系结构修改。我们通过强调语言模型在zero-shot设置中执行各种任务的能力来证明这种方法具有的潜力。我们根据任务获得有前途，有竞争力和最先进的结果。

### 方法：语言建模

![image-20220523150611686](C:\Users\Tracy Tao\AppData\Roaming\Typora\typora-user-images\image-20220523150611686.png)

![image-20220523150633463](C:\Users\Tracy Tao\AppData\Roaming\Typora\typora-user-images\image-20220523150633463.png)

<u>。我们的推测是，具有足够能力的语言模型将开始学习推断和执行自然语言序列中演示的任务，以便更好地预测它们，无论其采购(procurement)方法如何。如果语言模型能够做到这一点，它实际上将执行无监督的多任务学习。我们通过在各种任务的zero-shot设置中分析语言模型的性能来测试是否是这种情况。</u>

### 测试

1. 儿童书籍测试：GPT-2在普通名词上达到了93.3％的新技术水平，在命名实体上达到了89.1％。应用去标记器以从CBT中移除PTB样式标记化工件。
2. LAMBADA：调查GPT-2的错误表明大多数预测是句子的有效延续，但不是有效的最终单词。这表明LM没有使用额外的有用约束，即该词必须是句子的最后一个。
3. 但是对其答案和错误的一些检查表明GPT-2经常使用基于简单检索的启发式方法，例如回答文档中的名称以回答谁的问题。
4. 我们测试GPT-2是否已经开始学习如何从一种语言翻译成另一种语言。

![image-20220523151157135](C:\Users\Tracy Tao\AppData\Roaming\Typora\typora-user-images\image-20220523151157135.png)

----

**可以用无监督的预训练模型去做有监督任务**。

GPT

![img](https://upload-images.jianshu.io/upload_images/5357893-b4431bc4140fc442.png)

![image-20220523164033608](C:\Users\Tracy Tao\AppData\Roaming\Typora\typora-user-images\image-20220523164033608.png)

# BERT中的激活函数GELU：高斯误差线性单元

![img](https://upload-images.jianshu.io/upload_images/5357893-d73800df7efd3f5e.png?imageMogr2/auto-orient/strip|imageView2/2/w/346/format/webp)

**模型效果**

GPT基于Transformer修改，在一个8亿单词的语料库上训练，12个Decoder层，12个attention头，隐藏层维度为768。

GPT在自然语言推理、分类、问答、对比相似度的多种测评中均超越了之前的模型（具体的测试以及对比效果详见论文）。且从小数据集如STS-B（约5.7k训练数据实例）到大数据集（550k训练数据）都表现优异。甚至通过预训练，也能实现一些Zero-Shot任务。但由于无标签数据与具体问题的契合度低，因此，学起来更慢，需要的算力也更多。

