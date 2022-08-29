'''一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
（先后次序不同算不同的结果）。
'''

# 【思路】第1，2阶分别有1，和2种方法，通项f(n) = f(n-1) + f(n-2)满足斐波那契数列

class Solution:
    def jumpFloor(self, number):
        n = number
        res = [1, 1, 2]  
        while n >= len(res):
            res.append(res[-1] + res[-2])
        return res[n]
        
