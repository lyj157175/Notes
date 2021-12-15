# 二叉树的遍历本质：使用递归，每个节点本质上都会经过三次，先经过本节点，先去左树转一圈回来，在去右树转一圈回来
# 也是二叉树上玩转动态规划的基础
#     1
#   2   3
# 4  5 6 7
#                     [1, 2, 4, 4, 4, 2，5, 5, 5, 2, 1, 3, 6,6,6,3, 7,7,7,3,1]
# 先序遍历第一次出现： 1，2，4，5，3，6，7
# 中序遍历第二次出现： 4，2，5，1，6，3，7
# 后续遍历第三次出现： 4，5，2，6，7，3，1

# 层序遍历：主要核心思想利用对列来压入弹出节点

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = Node()
    
    def preorder(self):
        self.pre_(self.root)
    
    def pre_(self, node):
        if node is None:
            return
        print(node.val + ' ')
        self.pre_(node.left)
        self.pre_(node.right)

    def inorder(self):
        self.in_(self.root)
    
    def in_(self, node):
        if node is None:
            return
        self.in_(node.left)
        print(node.val + ' ')
        self.in_(node.right)

    def postorder(self):
        self.post_(self.root)
    
    def post_(self, node):
        if node is None:
            return
        
        self.post_(node.left)
        self.post_(node.right)
        print(node.val + ' ')



# 二叉树遍历的非递归形式：
# 先序遍历：准备一个栈，先将当前节点压入栈，弹出就打印，然后先压入右孩子，在压入左孩子，弹出就打印，依次进行
def pre(root):
    if root != None:
        stack_ = []
        stack_.append(root)
        while len(stack_) != 0:
            node = stack_.pop()
            print(node.val)
            if node.right != None:
                stack_.append(node.right)
            if node.left !=None:
                stack_.append(node.left)
    
# 后续遍历: 准备两个栈，先将当前节点压入栈，弹出压入另一个栈中，然后先压入左孩子，在压入右孩子，弹出压入另一个栈中，依次进行。
# 最后将另一个容器依次弹出
def post(root):
    if root !=None:
        stack1 = []
        stack2 = []
        stack1.append(root)
        while len(stack1) !=0:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left !=None:
                stack1.append(node)
            if node.right !=None:
                stack1.append(node)
        if len(stack2)!=0:
            print(stack2.pop())



# 二叉树的层序遍历，其实就是宽度优先遍历，使用队列处理
def ceng_bst(root):
    if root == None:
        return 
    queue = []
    queue.append(root)
    while len(queue)!=0:
        node = queue.pop(0)
        print(node.val, ' ')
        if node.left !=None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
        

# 找到二叉树最大宽度的层数，并返回最大层的节点数
def get_max_ceng(root):
    if root ==None:
        return 0
    queue = []
    queue.append(root)

    dict_ = {}  # 当前层的dict
    dict_[root] = 1
    level = 1   # 当前层
    cur_level_node_num = 0   # 当前层节点数
    max_ = 0
    while(len(queue))!=0:
        node = queue.pop(0)
        cur_level = dict_[node]
        
        if node.left !=None:
            dict_[node.left] = cur_level + 1
            queue.append(node.left)
        if node.right != None:
            dict_[node.right] = cur_level + 1
            queue.append(node.right)
        
        if level == cur_level:
            cur_level_node_num += 1
        else:
            max_ = max(max_, cur_level_node_num)
            cur_level+=1
            cur_level_node_num = 1
    max_ = max(max_, cur_level_node_num)
    return max_



# 二叉树的序列化和反序列化，先序，中序，后续，层序四种方式
# 序列化指将二叉树依次取出，如果没有子节点补空节点。反序列化是指将序列化的列表还原为二叉树
def pre_seq(self):
    pre_seq = []
    pre_seq = self.pre_(self.root, pre_seq)
    return pre_seq

def pre_(self, node, pre_seq):
    if node is None:
        pre_seq.append(None)
    else:
        pre_seq.append(node.val)
        self.pre_(node.left, pre_seq)
        self.pre_(node.right, pre_seq)
    return pre_seq


# 利用前序序列化来重建树
def pre_build(self, pre_seq):
    if len(pre_seq) == 0:
        return None
    return pre_build(pre_seq)

def pre_build_(self, pre_seq):
    val = pre_seq.pop()
    if val==None:
        return None
    node = Node(val)
    node.left = pre_build_(pre_seq)
    node.right = pre_build_(pre_seq)
    return node


# 利用层序遍历来序列化和反序列化
def ceng_seq(root):
    if root == None:
        return None
    queue = []
    queue.append(root.val)
    seq_len = []
    while len(queue)!=0:
        node = queue.pop(0)
        if node.left!=None:
            queue.append(node.left)
            seq_len.append(node.left.val)
        else:
            seq_len.append(None)
        if node.right != None:
            queue.append(node.right)
            seq_len.append(node.right.val)
        else:
            seq_len.append(None)
    return seq_len


# 层序遍历，利用seq_len这个队列来还原二叉树
def reserve_ceng_seq(seq_len):
    if len(seq_len) == 0:
        return None
    head = build_node(seq_len.pop(0))
    queue = []
    if head !=None:
        queue.append(head)
    while len(queue)!=0:
        node = queue.pop(0)
        node.left = build_node(seq_len.pop(0))
        node.right = build_node(seq_len.pop(0))
        if node.left !=None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return head

def build_node(val):
    if val==None:
        return None
    return Node(val)



    
# 二叉树的递归套路，解决95%的树型dp问题

# 给定二叉树的头节点，返回二叉树是不是一个平衡二叉树（每一颗树左右子树的高度差不超过1）
# 思路：左子树需要是平衡的，右子树需要是平衡的，并且左右子树的高度差不超过1

