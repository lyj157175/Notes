"""
问题描述：假设链表中每个节点的值都在[0,9]之间，那么链表整体就可以代表一个整数，
例如：9->3->7,可以代表整数937.给定两个这种链表的头结点head1和head2，请生
成代表两个整数相加值的结果链表。例如：链表1为9->3->7，链表2为6->3,最后生成
新的结果链表为1->0->0->0.

思路：
1）如果将链表先转化为整数相加，再转成链表，可能会出现溢出
2）可以使用逆序栈将链表节点压入栈，再进行操作
3）利用链表的逆序求解，这样不会占用额外空间复杂度
"""

# 直接转化为数字相加可能会数字溢出，不建议
# 思路：遍历链表将数字添加到两个栈中，然后依次弹出栈顶元素进行相加，考虑下进位情况，然后将相加后的结果简历为新节点
class Node:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = None


def addList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    stack1, stack2 = [], []
    while head1 != None:
        stack1.append(head1.val)
        head1 = head1.next
    while head2 != None:
        stack2.append(head2.val)
        head2 = head2.next 
    
    ca = 0   # 进位的标志
    new_head = None
    while len(stack1) != 0 or len(stack2) != 0:
        n1 = stack1.pop() if len(stack1) != 0 else 0
        n2 = stack2.pop() if len(stack2) != 0 else 0
        num = (n1 + n2 + ca) % 10
        ca = 1 if num == 0 else 0
        node = Node(num)
        node.next = new_head 
        new_head = node
    
    # 考虑进位的情况
    if ca == 1:
        node = Node(ca)
        node.next = new_head 
        new_head = node 
    return new_head 

# -------------------------------------------
# 优化，将链表反转从头开始进行相加操作，这样不会利用多余的栈结构
def reserve(head):
    pre = None
    while head !=None:
        next = head.next 
        head.next = pre 
        pre = head 
        head = next 
    return pre 

def addList2(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    rhead1 = reserve(head1)
    rhead2 = reserve(head2)
    ca = 0
    new_head = None
    while rhead1 != None or rhead2 != None:
        n1 = rhead1.val if rhead1 != None else 0
        n2 = rhead2.val if rhead2 != None else 0
        num = (n1 + n2 + ca) % 10
        ca = 1 if num == 0 else 0
        node = Node(num)
        new_head.next = node
        new_head = node 
        
        rhead1 = rhead1.next if rhead1.next != None else None
        rhead2 = rhead2.next if rhead2.next != None else None
    
    if ca == 1:
        node = Node(ca)
        new_head.next = node
    
    return reserve(new_head)


