'''给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''


# 【思路】当前节点有右子树时，下一个节点就是右子树的最左下边的点。如果无右子树，则找到当前节点的父节点，如果是父节点的左子节点则下一个节点是父节点，如果是
# 父节点的右子节点，下一个节点是父节点的父节点。

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        while pNode.next:
            root = pNode.next
            if root.left == pNode:
                return root
            pNode = root
        return None