"""
问题描述：单链表可能有环，也可能无环。给定两个单链表的头结点head1和head2,
这两个链表可能相交，也可能不相交。请实现一个函数，如果两个链表相交，请返回相
交的第一个节点，如果不相交，返回None即可。

要求：如果链表1的长度为N，链表2的长度为M，时间复杂度请达到O(M+N),额外空间复
杂读请达到O(1)

思路：
1）使用快慢指针判断是否有环，有环可以通过快慢指针求出环和非环部分的交点
"""

### 链表最难的两个问题  1. 约瑟夫环问题   2. 下面两链表相交问题: 
# 给定两个可能有环或者无环的单链表，head1和head2，如果相交则返回第一个节点，如果不相交，返回None。
# 如果两个链表长度之和为N，时间复杂度请达到0（N），额外空间复杂度请达到0（1）。
# 思路： https://www.cnblogs.com/zh-xiaoyuan/p/15129849.html
#      1.先判断单链表是否有环。利用快慢指针，当两者相遇则将快指针移到head处，两者继续开始以1的速度移动，当再次相遇时则是入环节点
#      2. 判断两链表是否相交，相交返回第一个相交的节点，不相交返回None
#            2.1两个链表无环，如果相交，则相交节点到最后的None共用：先判断两链表的尾节点是不是相等，
#            如果不相等则肯定不想交。如果相等，则将两个链表长度相减等于n，让长链表先走n步，然后两链表一起走，相遇时则是节点）
#            2.2.两个链表一个有环，一个无环，则不可能相交
#            2.3.两个链表都有环。有三种情况
#                 2.3.1. 不相交
#                 2.3.2. 一个相交点，跟2.1的处理方式一样
#                 2.3.3. 两个相交点，当从loop1继续开始走，如果再回到loop1时遇到loop2则是2.3.3，否则是情况2.3.1

def main(head1, head2):
    loop1 = isloop_list(head1)
    loop2 = isloop_list(head2)
    if loop1 == None and loop2 == None:  # 两链表无环
        return noloop(head1, head2)
    if loop1 != None and loop2 != None:  # 两链表都有环
        return bothloop(head1, loop1, head2, loop2)
    return None
    

# 判断是否有环，有环返回入环节点，无环返回None
def isloop_list(head):
    if head==None or head.next==None or head.next.next==None:  # 最多一个节点时，无环
        return None   
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next==None or fast.next.next== None:
            return None
        slow = slow.next
        fast = fast.next.next
    # 有环则fast到head处开始继续走,相遇时节点即入环节点
    fast = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow

# 两链表都无环情况，相交返回第一个相交节点，否则返回None
def noloop(head1, head2):
    if head1 == None or head2 == None:  # 有一个链表为空则返回None
        return None
    cur1 = head1
    cur2 = head2
    n = 0
    # 遍历两个链表来判断尾节点是不是一样, 如果不一样则不相交
    while cur1!=None:
        n+=1
        cur1 = cur1.next
    while cur2!=None:
        n-=1
        cur2 = cur2.next
    if cur1!=cur2:
        return None
    # 长链表为cur1，短链表为cur2
    if n>=0:
        cur1 = head1
        cur2 = head2
    else:
        n = -n
        cur1 = head2
        cur2 = head1
    # 长链表先移动n步
    while n!=0:
        cur1 = cur1.next
        n-=1
    # 当两链表相交则是相交节点
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1 

# 两个链表都有环的情况,有交点返回第一个交点，没有返回None
def bothloop(head1, loop1, head2, loop2):
    cur1 = None
    cur2 = None
    if loop1 == loop2:  # 相当于有一个交点2.3.2的情况， 先让cur1和cur2都到loop1和loop2，然后和2.1的一样处理
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1!=loop1:
            n+=1
            cur1 = cur1.next
        while cur2!= loop2:
            n-= 1
            cur2 = cur2.next
        # 让cur1为长的链表
        if n>=0:
            cur1 = head1
            cur2 = head2
        else:
            n -= 1
            cur1 = head2
            cur2 = head1
        while n!=0:
            cur1 = cur1.next
            n -= 1
        while cur1!=cur2:
            cur1 = cur1.next
            cur2 = cur2.next
    else:   # 相当于情况1或3,继续让loop1向前移动，在loop1回到自己之前如果遇到loop2则说明有两个节点
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:  # 中途遇到loop2，2.3.3的情况，随便返回loop1或者loop2
                return loop1
            cur1 = cur1.next
    return None