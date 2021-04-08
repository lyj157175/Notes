'''在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

对于50%的数据, size≤10^4
对于75%的数据, size≤10^5
对于100%的数据, size≤2*10^5
 
输入描述:
题目保证输入的数组中没有的相同的数字
输入
[1,2,3,4,5,6,7,0]
返回值
7
'''

class Solution:
    def InversePairs(self, data):
        # 方法一（运行超时）：将数组copy一份，对copy的数组排序，按copy数组的顺序依次找到data数组中元素的index，
# 其索引即为该数的逆序对数，将其全部相加。
        # if len(data) == 0:
        #     return 0
        # count = 0
        # copy = []
        # for i in data:
        #     copy.append(i)
        # copy.sort()
        # i = 0
        # while len(data) > 0:
        #     count += data.index(copy[i])
        #     data.remove(copy[i])
        #     i += 1
        # return count%1000000007

        # 方法二：暴力法
        if len(data) == 0:
            return 0
        count = 0
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                if data[i] > data[j]:
                    count += 1
        return count%1000000007


        # 方法三:
        
        





        
