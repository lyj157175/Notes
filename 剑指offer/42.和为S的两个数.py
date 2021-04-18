'''输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，
输出两个数的乘积最小的。
返回值描述:
对应每个测试案例，输出两个数，小的先输出。
示例1
输入
[1,2,4,7,11,15],15
返回值
[4,11]
'''


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if array is None:
            return None
        i, j = 0, len(array)-1
        mul = []
        res = []
        while i <= j:
            if array[i] + array[j] == tsum: 
                mul.append(array[i] * array[j])
                res.append([array[i], array[j]])
                i += 1
            elif array[i] + array[j] > tsum:
                j -= 1
            else:
                i += 1
        return res[mul.index(min(mul))]

