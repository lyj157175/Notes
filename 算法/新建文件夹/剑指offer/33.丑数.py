'''把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
输入
7
返回值
8
'''

# 【思路】下一个丑数，一定是由之前某一个丑数乘以2或者乘以3或者是乘以5中的最小值，
# 因此可以用动态规划的方法实现，但是这里要引入三个指针，来记录乘2、乘3、乘5的位置，并不断更新。

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0: 
           return 0
        res = [1]
        n2, n3, n5 = 0, 0, 0
        i = 0
        while i < index:
            val = min(res[n2]*2, res[n3]*3, res[n5]*5)
            res.append(val)
            if res[n2]*2 == val:
                n2 += 1
            if res[n3]*3 == val:
                n3 += 1
            if res[n5]*5 == val:
                n5 += 1
            i += 1
        return res[index-1]
