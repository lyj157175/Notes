'''请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
示例1
输入
{8,6,10,5,7,9,11}
返回值
[[8],[10,6],[5,7,9,11]]
'''

# 【思路】设置几个变量，存放当前层的节点，存放当前节点的值，存放下一层节点


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        if pRoot is None:
            return []
        res = []
        cur_layer_node = [pRoot]
        is_even = True  # 偶数层

        while cur_layer_node:
            cur_layer_val = []
            next_layer_node = []
            is_even = not is_even
            for node in cur_layer_node:
                cur_layer_val.append(node.val)
                if node.left:
                    next_layer_node.append(node.left)
                if node.right:
                    next_layer_node.append(node.right)
            cur_layer_node = next_layer_node
            res.append(cur_layer_val[::-1]) if is_even else res.append(cur_layer_val)
        return res 