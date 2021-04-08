'''输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
输入
{1,3,5},{2,4,6}
返回值
{1,2,3,4,5,6}
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        node = cur = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
                cur = cur.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
                cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2
        return node.next

