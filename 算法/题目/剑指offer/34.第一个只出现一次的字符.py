'''在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
输入
"google"
返回值
4
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        res = []
        for k, v in count.items():
            if v == 1:
                res.append(k)
        for i in s:
            if i in res:
                return s.index(i)
        return -1
        


