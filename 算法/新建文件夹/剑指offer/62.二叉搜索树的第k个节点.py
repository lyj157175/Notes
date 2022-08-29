'''给定一棵二叉搜索树，请找出其中的第k小的TreeNode结点。
示例1
输入
{5,3,7,2,4,6,8},3
返回值
{4}
说明
按结点数值大小顺序第三小结点的值为4  
'''

# 【思路】中序遍历就是升序排列，找到第k-1个节点即可


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def KthNode(self, pRoot, k):
        res = []
        if pRoot is None:
            return None

        def preorder(node):
            if node is None:
                return None
            preorder(node.left)
            res.append(node)
            preorder(node.right)

        preorder(pRoot)
        if k > len(res) or k < 1:
            return None
        return res[k-1]
