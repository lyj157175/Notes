# k-近邻算法概述
# 采用测量不同特征值之间的距离方法进行分类。
# 优点：精度高、对异常值不敏感、无数据输入假定。
# 缺点：计算复杂度高、空间复杂度高。
# 适用数据范围：数值型和标称型。

# kNN的工作原理是：存在一个样本数据集合，也称作训练样本集，并且样本集中每个数据都存在标签，
# 即我们知道样本集中每一数据与所属分类的对应关系。输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应
# 的特征进行比较，然后算法提取样本集中特征最相似数据（最近邻）的分类标签。最后，选择k个最相似数据中出现次数最多
# 的分类，作为新数据的分类。


import numpy as np


def dataset():
    group = np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
    label = ['爱情片','爱情片','爱情片','动作片','动作片','动作片']
    return group, label
   

def knn(test, group, label, k):
    n = group.shape[0]   # 行数  
    diff = np.tile(test, (n, 1)) - group
    distance = (diff ** 2).sum(axis=1) ** 0.5
    index = distance.argsort()   # 小到大的索引

    class_count = {}
    for i in range(k):
        class_ = label[index[i]]
        if class_ not in class_count:
            class_count[class_] = 1
        else:
            class_count[class_] += 1
    class_sort = sorted(class_count.items(), key=lambda x: x[1], reverse=True)  # 按值进行降序排列
    return class_sort[0][0]   # 返回类别

    

if __name__ == '__main__':
    group, label = dataset()
    test = [101, 20]
    test_class = knn(test, group, label, k=3)
    print(test_class)

