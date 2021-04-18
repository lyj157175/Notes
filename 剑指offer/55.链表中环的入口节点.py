'''给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''

# 【思路】快慢指针, 第一次相遇说明有环且处于slow和fast的交点处。将fast重置到pHead，当slow和fast再次相遇则是环入口点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        slow = pHead
        fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
        
