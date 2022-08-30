'''数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组
{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

输入
[1,2,3,2,2,2,5,4,2]
返回值
2
'''

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        val = len(numbers) // 2 + 1
        res = {}
        
        for i in numbers:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1
    
        for k, v in res.items():
            if v >= val:
                return k
        return 0

