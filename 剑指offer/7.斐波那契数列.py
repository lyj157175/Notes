'''大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n≤39

输入
4
返回值
3
'''


class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0

        a = 0
        b = 1
        for i in range(n):
            a, b = b, a+b
        return a
