'''输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入
如下4 X 4矩阵：  1 2 3 4 
                5 6 7 8 
                9 10 11 12 
                13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

输入
[[1,2],[3,4]]
返回值
[1,2,4,3]
'''

#【思路】当matrix存在元素时，依次添加到一个数组即可

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    res.append(i.pop())
            if matrix and matrix[0]:
                for i in matrix.pop()[::-1]:
                    res.append(i)
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    res.append(i.pop(0))
        return res

