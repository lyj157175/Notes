'''在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任一一个重复的数字。 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，
那么对应的输出是2或者3。存在不合法的输入的话输出-1
示例1
输入
[2,3,1,0,2,5,3]
返回值
2或3
'''


class Solution:
    def duplicate(self , numbers):
        if numbers == None:
            return -1
        count = {}
        for i in numbers:
            if i not in count:
                count[i] = 1
            else:
                return i
        return -1
        
        # for k, v in count.items():
        #     if v > 1:
        #         return k
        # return -1
        # return -1
