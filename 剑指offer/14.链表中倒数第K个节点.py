'''输入一个链表，输出该链表中倒数第k个结点。
如果该链表长度小于k，请返回空。
输入
{1,2,3,4,5},1 
返回值
{5}
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, pHead, k):
        if pHead is None:
            return None
        res = []
        while pHead:
            res.append(pHead)
            pHead = pHead.next
        if k < 1 or k > len(res):
            return None
        return res[-k]
        
        
        
        



               
        