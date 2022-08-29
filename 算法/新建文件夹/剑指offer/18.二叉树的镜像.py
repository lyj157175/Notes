'''操作给定的二叉树，将其变换为源二叉树的镜像。
比如：    源二叉树 
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
输入
{8,6,10,5,7,9,11}
返回值
{8,10,6,11,9,7,5}
'''

# 【思路】将左右子节点依次交换,返回原来的根节点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, pRoot):
        self.swap(pRoot)
        return pRoot
    
    def swap(self, node):
        if node != None:
            left = node.left
            right = node.right 
            node.left = right
            node.right = left
            self.swap(left)
            self.swap(right)

