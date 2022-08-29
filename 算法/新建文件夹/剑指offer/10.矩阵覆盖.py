'''我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
'''

# 【思路】f(0)=0, f(n)=1, f(2)=2, f(3)=3, f(n)=f(n-1)+f(n-2)

class Solution:
    def rectCover(self, number):
        n = number
        if n==0 or n==1 or n==2:
            return n
        a = 1
        b = 2
        for i in range(n-2):
            a, b = b, a+b
        return b
