"""
问题描述：分别实现反转单向链表和反转双向链表的函数

要求：如果链表为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)
"""


def reservelist(head):
    if head is None or head.next is None:
        return head 
    
    pre = None
    while head is not None:
        next = head.next 
        head.next = pre 
        pre = head 
        head = next 
    return pre 



def reserveDoubleList(head):
    if head is None or head.next is None:
        return head 
    
    pre = None
    while head is not None:
        next = head.next 
        head.next = pre 
        head.last = next 
        pre = head 
        head = next 
    return pre 

