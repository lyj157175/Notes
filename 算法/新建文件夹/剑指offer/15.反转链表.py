'''输入一个链表，反转链表后，输出新链表的表头。
输入
{1,2,3}
返回值
{3,2,1}
'''

# 【思路】需要三个节点表示，前一个pre，当前节点pHead，下一个nxt

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre = None
        while pHead:
            nxt = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = nxt
        return pre

