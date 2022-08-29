'''给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字
是1,2,3,4。如果K>数组的长度，那么返回一个空的数组
示例1
输入
[4,5,1,6,2,7,3,8],4 
返回值
[1,2,3,4]
'''


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        tinput.sort()
        return tinput[:k]


        






