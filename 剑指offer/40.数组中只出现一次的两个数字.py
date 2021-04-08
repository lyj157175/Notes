'''一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
[1,4,1,6]
返回值
[4,6]
说明
返回的结果中较小的数排在前面  
'''


class Solution:
    def FindNumsAppearOnce(self, array):
        count = {}
        for i in array:
            if i in array:
                count[i] += 1
            else:
                count[i] = 1
        res = []
        for k, v in count.items():
            if v == 1:
                res.append(k)
        return res.sort()


