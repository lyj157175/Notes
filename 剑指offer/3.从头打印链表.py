'''输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

输入
{67,0,24,58}
返回值
[58,24,0,67]
'''

class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print_linkedlist(self, listNode):
        res = []
        cur = listNode

        while cur:
            res.append(cur.val)
            cur = cur.next
        return res[::-1]




