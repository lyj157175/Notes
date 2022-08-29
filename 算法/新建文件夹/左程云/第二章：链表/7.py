"""
问题描述：给定一个链表的头结点，请判断该链表是否为回文结构，例如：
1->2->1,返回true
1->2->2->1,返回true
15->6->15,返回true
1->2->3,返回false

进阶：
如果链表长度为N，时间复杂度达到O(N)，额外空间复杂度达到O(1)

思路：进阶问题的关键是将链表的右半部分反转，然后再进行比较，注意把
改变的状态变回来
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = None

# 思路：找到链表右半部分，将右半部分依次压入栈中，然后将栈顶元素依次和链表头重新开始比较 
def ishuiwen(head):
    if head is None or head.next is None:
        return True
    
    right = head.next 
    cur = head 
    while cur.next != None and cur.next.next != None:
        right = right.next 
        cur = cur.next.next 
    
    res = []
    while right != None:
        res.append(right.val)
        right = right.next 
    
    while len(res) != 0:
        if res.pop() == head.val:
            head = head.next 
        else:
            return False
    
    return True
    

