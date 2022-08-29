'''将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
返回值描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
"+2147483647"
返回值
2147483647
'''


class Solution:
    def StrToInt(self, s):
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        fu = ['+', '-']
        res = 0
        symbol = 1
        
        for i in s:
            if i in nums:
                res = res*10 + nums.index(i)
            elif i in fu:
                if i == '-':
                    symbol = -1
            else:
                return 0
        return res * symbol

