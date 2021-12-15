"""
问题描述：给定一个无序单链表的头结点head，删除其中值重复出现的节点。
例如：1->2->3->3->4->4->2->1->1->None，删除值重复的节点之后为
1->2->3->4_None.
要求：分别按以下要求实现两种方法
1)如果链表长度为N，时间复杂度为O(N)
2)额外空间复杂度为O(1)

思路：
1）使用hashmap辅助
2）遍历即可
"""

# 方法一
def removeSame(head):
    if head is None or head.next is None:
        return head
        
    dict_ = {}
    cur = head 
    pre = None
    while cur != None:
        if cur.val not in dict_:
            dict_.add(cur.val)
            pre = cur 
        else:
            pre.next = cur.next 
        cur = cur.next 
    return head 


# 方法二: 两个for循环遍历， o（n^2）， 不推荐
    

