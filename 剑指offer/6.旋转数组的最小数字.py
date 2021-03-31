'''把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

输入
[3,4,5,1,2]
返回值
1
'''

class Solution:

    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        return min(rotateArray)

while True:
    try:
        S = Solution()
        data = list(eval(raw_input()))
        print(S.minNumberInRotateArray(data))
    except:
        break

