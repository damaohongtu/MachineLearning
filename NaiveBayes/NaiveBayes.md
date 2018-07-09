# 朴素贝叶斯讲解（以词汇歧义消解为例）
## 1.计算过程

| 步骤 | 计算 | 举例 |
| ---- | ---- | ---- |
| 目标 | ![](../pictures/NB_1.png)| ![](../pictures/NB_obj.png) “打”的含义有多个，需要根据上下文确定“打”的含义,这里上下文指“打”前后的汉子|
| 贝叶斯公式 | ![](../pictures/NB_2.png) |   |
| 分母不变性，去掉公有项 | ![](../pictures/NB_3.png) |   |
| 使用极大似然法进行估计 | ![](../pictures/NB_4.png)![](../pictures/NB_5.png)![](../pictures/NB_6.png) | N(si) 是在训练数据中词w用于义si时的次数，而N(vk, si)为w用于语义si时词vk出现在w的上下文中的次数。N(w)为多义词w在训练数据中出现的总次数。模型最后就是保存为这两个概率。|
| 歧义消解 |  ![](../pictures/NB_7.png)<br/>![](../pictures/NB_8.png)<br/> |  求最大的概率即可 |

## 2.举例
![](../pictures/NB_example1.png)<br>
![](../pictures/NB_example2.png)<br>
![](../pictures/NB_example3.png)<br>
![](../pictures/NB_example4.png)
