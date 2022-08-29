'''请实现两个函数，分别用来序列化和反序列化二叉树
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以！表示
一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
示例1
输入
{8,6,10,5,7,9,11}
返回值
{8,6,10,5,7,9,11}
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        res = []
        def pre_order(node):
            if node is None:
                res.append('#')
                return None
            pre_order(node.left)
            pre_order(node.right)
            res.append(str(node.val))
        pre_order(root)
        return ' '.join(res)
    
    def Deserialize(self, s):
        res = s.split()
        def build_tree():
            val = res.pop(-1)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.right = build_tree()
            node.left = build_tree()
            return node
        node = build_tree()
        return node
        