'''一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
输入
3
返回值
4
'''

# 【思路】n=0,1时，f(n)=1, n>=2时， f(n)=2*f(n-1)

class Solution:
    def jumpFloorII(self, number):
        n = number
        if n < 2:
            return 1
        return 2*self.jumpFloorII(n-1)
