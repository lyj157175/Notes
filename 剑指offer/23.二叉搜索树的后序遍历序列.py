'''输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。
假设输入的数组的任意两个数字都互不相同。（ps：我们约定空树不是二叉搜索树）
输入
[4,8,6,12,16,14,10]
返回值
true
'''

#【思路】二叉搜索树：
# （1）若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# （2）若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# （3）它的左、右子树也分别为二叉排序树。
# 从数组左侧向右找，找到比root值大的位置，将左子树的值，右子树的值区分开，再用递归完成下一子规模查找


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.rebuild(sequence)


    def rebuild(self, sequence):
        if len(sequence) <= 2:
            return True
        root = sequence.pop()
        idx = 0
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
            idx += 1
        left = sequence[:idx]
        right = sequence[idx:]
        for v in right:
            if v < root:
                return False
        return self.rebuild(left) and self.rebuild(right)

