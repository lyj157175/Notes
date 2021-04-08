'''输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为 O(n).
输入
[1,-2,3,10,-4,7,2,-5]
返回值
18
'''

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        n = len(array)
        dp = array
        for i in range(1, n):
            dp[i] = max(dp[i-1] + array[i], array[i])
        return max(dp)
