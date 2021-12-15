"""
问题描述：给定两个有序链表的头指针head1和head2,打印两个
链表的公共部分(即链表节点的值相同的部分)

思路：由于链表有序，所以可以比较head1和head2的值进行判断
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printSame(head1, head2):
    if head1 is None or head2 is None:
        return None
    while head1 and head2:
        if head1.val == head2.val:
            print(head1.val, end=' ')
            head1 = head1.next
            head2 = head2.next
        elif head1.val < head2.val:
            head1 = head1.next
        else:
            head2 = head2.next
    
if __name__ == "__main__":
    head1 = Node(2)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(6)

    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(6)
    head2.next.next.next = Node(8)

    printSame(head1, head2)
