'''请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
示例1
输入
{8,6,6,5,7,7,5}
返回值
true
示例2
输入
{8,6,9,5,7,7,5}
返回值
false
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
        return self.is_morror(pRoot, pRoot)

    def is_morror(self, pleft, pright):
        if not pleft and not pright:
            return True
        if not pleft or not pright:
            return False
        if pleft.val != pright.val:
            return False
        return self.is_morror(pleft.left, pright.right) and self.is_morror(pleft.right, pright.left)
        
