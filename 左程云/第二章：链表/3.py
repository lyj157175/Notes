"""
问题描述：给定链表的头结点head,实现删除链表的中间节点的函数，例如：
不删除任何节点；
1->2,删除节点1；
1->2->3,删除节点2；
1->2->3->4，删除节点2；
1->2->3->4->5，删除节点3；
进阶：
给定链表头节点head、整数a和b，实现删除位于a/b节点处的函数，例如：
链表1->2->3->4->5,假设a/b的值为r。
如果r等于0，不删除任何节点；
如果r在区间(0, 1/5]之间，删除节点1；
如果r在区间(1/5, 2/5]之间，删除节点2；
如果r在区间(2/5, 3/5]之间，删除节点3；
如果r在区间(3/5, 4/5]之间，删除节点4；
如果r在区间(4/5, 1]之间，删除节点5；
如果r大于1，不删除任何节点。
"""
import math

def deleteMid(head):
    if head is None or head.next is None:
        return head
    
    if head.next is None:
        return head.next 
    
    pre = head 
    cur = head.next.next 
    while cur.next is not None and cur.next.next is not None:
        pre = pre.next 
        cur = cur.enxt.next 
    pre.next = pre.next.next 
    return head 


def deleteNode(head, a, b):
    if head is None or a > b or b == 0:
        return head
    
    node = head 
    n = 0
    while node is not None:
        node = node.next 
        n += 1

    r = math.ceil(a / b) * n 
    if r == 1:
        return head.next 

    pre = None
    node = head 
    while r > 1:
        pre = node
        node = node.next 
        r -= 1
    pre.next = node.next 
    return head 





    

    