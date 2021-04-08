'''输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的
绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
输入
{1,2,3,4,5,6,7}
返回值
true
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if abs(self.max_depth(pRoot.left) - self.max_depth(pRoot.right)) > 1:
            return False
        else:
            return True

    # 求树的最大深度
    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

        