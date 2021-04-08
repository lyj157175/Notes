'''输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
输入
{8,8,#,9,#,2,#,5},{8,9,#,2}
返回值
true
'''

#【思路】当两颗树都存在的时候进行比较。找到两树值相同的位置开始进一步递归比较子节点（进入函数is_same），判断
# 完毕返回结果。如果两树值不相同则利用a树的左子节点和右子节点继续与b树值进行判断。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_same(self, ta, tb):
        if tb is None:
            return True
        if ta is None:
            return False
        if ta.val != tb.val:
            return False
        return self.is_same(ta.left, tb.left) and self.is_same(ta.right, tb.right)

    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.is_same(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
        
        