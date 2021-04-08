'''小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的
序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
返回值描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
示例1
输入
9
返回值
[[2,3,4],[4,5]]
'''


class Solution:
    def FindContinuousSequence(self, tsum):
        lower, upper = 1, 2
        seq_sum = 3
        res = []

        while lower < upper:
            if seq_sum > tsum:
                seq_sum -= lower
                lower += 1
            elif seq_sum < tsum:
                upper += 1
                seq_sum += upper
            else:
                res.append([i for i in range(lower, upper+1)])
                upper += 1
                seq_sum += upper
        return res

        