"""
问题描述：分别实现两个函数，一个可以删除单链表中倒数第K个节点，另一个
可以删除双链表中倒数第K个节点

要求：如果链表长度为N，时间复杂度达到O(N),额外空间复杂度达到O(1)
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.last = None
        self.next = None


# 解法：先让链表从头走到尾，k--。如果k==0，说明需要删掉头节点，如果k>0,返回头节点。如果k<0，继续重新从头走到尾，k++。
# 当k==0时，节点停留在需要删除的点上，进行删除操作
def deleteSigList(head, k):
    if head is None or k < 1:
        return head
    
    node = head
    while node is not None:
        node = node.next
        k -= 1
    if k == 0:
        return head.next
    elif k > 0:
        return head
    else:
        pre = None
        node = head
        while k != 0:
            pre = node
            node = node.next
            k += 1
        pre.next = node.next
    return head
        

def deleteDouble(head, k):
    if head is None or k < 1:
        return head
    
    node = head
    while node is not None:
        node = node.next
        k -= 1
    
    if k == 0:
        head.next.last = None
        return head.next
    elif k > 0:
        return head
    else:
        node = head
        while k != 0:
            node = node.next
        node.next.last = node.last
        node.last.next = node.next

    return head


def print_list(head):
    while head is not None:
        print(head.val, end = ' ')
        head = head.next
    print()


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = deleteSigList(head, 2)
    print_list(head)


    head = DoubleNode(1)
    head.next = DoubleNode(2)
    head.next.next = DoubleNode(3)
    head.next.next.next = DoubleNode(4)
    head.next.next.next.next = DoubleNode(5)
    head = deleteSigList(head, 3)
    print_list(head)


