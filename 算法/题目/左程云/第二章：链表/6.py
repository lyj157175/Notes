"""
问题描述：41个人排成一个圈，由第一个人开始报数，报数到3的人就自杀，
然后再由下一个人重新报1，报数到3的人再自杀，这样依次下去，直到剩下
最后一个人时，他可以自由选择自己的命运。这就是著名的约瑟夫问题，现在
请用单向环形链表描述该结构并呈现整个自杀过程

要求：输入一个环形单向链表的头结点head和报数的值m，返回最后生存的节
点，该节点自己组成一个单向环形链表，其他节点都删掉
进阶：
如果链表头结点数为N,想在时间复杂度为O(N)时完成原问题的要求，如何实现

思路：参见https://blog.oldj.net/2010/05/27/joseph-ring/
"""

def baoshu(head, m):
    if head is None or head.next == head or m < 1:
        return head 
    
    count = 0
    pre = head 
    while pre.next != head:
        pre = pre.next   # 找到head的前一个节点
    
    # head是当前报数的节点
    while pre != head:
        count += 1
        if count == m:
            count = 0
            pre.next = head.next 
        else:
            pre = pre.next 
        head = pre.next 
    return head 


# 非实现
# def kill_2(cls, head, m):

#     if head is None or head.next == head or m < 1:
#         return head

#     length = 1
#     node = head.next
#     while node != head:
#         length += 1
#         node = node.next
#     alive_num = cls.get_alive(length, m)
#     count = 1
#     node = head
#     while count < alive_num:
#         count += 1
#         node = node.next

#     return node

# @staticmethod
# def get_alive(n, m):
#     if n == 1:
#         return 1
#     return (JosephusCircle.get_alive(n-1, m) + m) % n