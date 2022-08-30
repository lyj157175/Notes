"""
问题描述：给定一个链表的头结点head和一个整数num,请实现函数将值为num的节点
全部删除。例如，链表为
1->2->3->4->None,num=3 链表调整后为1->2->4->None
"""

def removeNum(head, num):
    if head is None:
        return head 
    
    # 需要更新头节点为第一个不是num值的节点
    while head != None:
        if head.val == num:
            head = head.next 
        else:
            break 

    pre = None
    cur = head 
    while cur != None:
        if cur.val == num:
            pre.next = cur.next 
        else:
            pre = cur 
        cur = cur.next 
    return head 