'''输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
输入
[3,32,321]
返回值
"321323"
'''

# 【思路】冒泡法，将数字转化为字符串，前后相邻两个字符串相加，大的往后排


class Solution:
    def PrintMinNumber(self, numbers):
        n = len(numbers)
        numbers = [str(i) for i in numbers]
        for i in range(n-1):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] > numbers[j] + numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        res = ''
        for i in numbers:
            res += i
        return res
