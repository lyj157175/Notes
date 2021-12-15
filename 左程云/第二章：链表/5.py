"""
问题描述：给定一个单链表的头结点head,以及两个整数from和to，在单链表上
把第from个节点到第to个节点这一部分进行反转。
例如：
1->2->3->4->5->None, from=2, to=4
调整结果为：1->4->3->2->5->None

再如：
1->2->3->None, from=1, to=3
调整结果为:
3->2->1->None

要求：
1.如果链表长度为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)
2.如果不满足1<=from<=to<=N，则不用调整
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

# 思路：找到from_的前一个节点pre和to_的后一个节点nxt，将中间部分进行反转，然后连接pre和nxt
# 需要考虑特殊情况，当pre是否为none，如果是说明需要换头节点，否者不需要换头节点
def reserveFromTo(head, from_, to_):
    if head is None or from_ >= to_ or from_ < 1:  # 还没有排除to_ - from_ > length的情况
        return head
    
    pre, nxt = None, None
    node = head 
    length = 0
    while node is not None:
        length += 1
        if length == from_ - 1:
            pre = node 
        if length == to_ + 1:
            nxt = node 
        node = node.next 

    if (to_ - from_) > length:
        return head 
    
    # 找到反转开始节点
    if pre is None:
        start = head 
    else:
        start = head.next 
    
    node = start.next 
    start.next = nxt 

    while node != nxt:
        next = node.next 
        node.next = start
        start = node
        node = next 
    
    if pre is None:
        return start
    
    pre.next = start 
    return head 


def print_node(head):
    while head is not None:
        print(head.val, end = ' ')
        head = head.next 
    print()



if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print_node(reserveFromTo(head, 2, 4))

