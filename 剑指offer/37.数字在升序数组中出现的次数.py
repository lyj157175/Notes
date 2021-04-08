'''统计一个数字在升序数组中出现的次数。
输入
[1,2,3,3,3,3,4,5],3
返回值
4
'''


class Solution:
    def GetNumberOfK(self, data, k):
        count = 0
        for i in data:
            if i == k:
                count += 1
        return count