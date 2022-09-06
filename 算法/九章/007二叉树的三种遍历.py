class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉搜索树
class BST:

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, node):
        if node is None:
            return

        print(node.val)
        self.post_order(node.left)
        self.post_order(node.right)

    def in_order(self, node):
        if node is None:
            return

        self.post_order(node.left)
        print(node.val)
        self.post_order(node.right)

    def post_order(self, node):
        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)



### 二叉树非递归的中序遍历
# 【题目】通过实现hasNext和next两个方法来实现二叉树的中序遍历
# 思路：非递归利用自己的栈




