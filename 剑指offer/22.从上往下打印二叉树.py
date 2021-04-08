'''从上往下打印出二叉树的每个节点，同层节点从左至右打印。
输入
{5,4,#,3,#,2,#,1}
返回值
[5,4,3,2,1]
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        if root is None:
            return []
        temp = [root]
        while temp:
            t = temp
            temp = []
            for i in t:
                res.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
        return res

