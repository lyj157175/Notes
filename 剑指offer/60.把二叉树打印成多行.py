'''从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
示例1
输入
复制
{8,6,10,5,7,9,11}
返回值
复制
[[8],[6,10],[5,7,9,11]]
'''

# 【思路】和59题一模一样

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
        while cur_layer_node:
            cur_layer_val = []
            next_layer_node = []
            for node in cur_layer_node:
                cur_layer_val.append(node.val)
                if node.left:
                    next_layer_node.append(node.left)
                if node.right:
                    next_layer_node.append(node.right)
            cur_layer_node = next_layer_node
            res.append(cur_layer_val)
        return res 


