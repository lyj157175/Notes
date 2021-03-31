'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
  [1,2,8,9],
  [2,4,9,12],
  [4,7,10,13],
  [6,8,11,15]
]
给定 target = 7，返回 true。
给定 target = 3，返回 false。
'''

# 【思路】索引从array第一行的最后一个元素开始，比target大则左移，反之下移


class Solution:

    def find(self, target, array):
        m = len(array) - 1
        n = len(array[0]) -1
        i = 0

        while i <= m and n >= 0:
            if array[i][n] == target:
                return True
            if target < array[i][n]:
                n -= 1
                continue
            if target > array[i][n]:
                i += 1
                continue
        return False

