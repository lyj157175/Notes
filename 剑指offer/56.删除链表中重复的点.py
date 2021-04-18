'''在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
示例1
输入
{1,2,3,3,4,4,5}
返回值
{1,2,5}
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None:
            return pHead
        cur = pHead
        node = ListNode(0)
        pre = node
        pre.next = pHead

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
            else:
                pre.next = cur
                pre = pre.next
            cur = cur.next
        pre.next = cur 
        return node.next
            