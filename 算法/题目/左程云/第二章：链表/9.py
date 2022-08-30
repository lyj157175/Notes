"""
问题描述：一种特殊的链表节点类描述如下：
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None

Node类中的value是节点值，next指针和正常单链表中next指针的意义一样，都指向下一个节点，rand
指针是Node类中新增的指针，这个指针可能指向链表中任意一个节点，也可能指向None.

给定一个由Node节点类型组成的无环单链表的头结点head，请实现一个函数完成这个链表中所有结构的复
制，并返回复制的新链表的头结点。例如：链表 1->2->3->None,假设1的rand指针指向3，2的rand指
针指向None,3的rand指针指向1。复制后的链表应该也是这种结构，比如,1'->2'->3'->None,1'的
rand指针指向3',2'的rand指针指向None，3'的rand指针指向1',最后返回1'

进阶：不使用额外的数据结构，只用有限几个变量，且在时间复杂度为O(N)内完成原问题要实现的函数。

思路：
1）如果不考虑空间复杂度，可使用hashmap求解
2）由于复制的链表和原链表具有操作一致性，所以可以直接在原链表中每个元素后插入一个和前一个一样的
元素，两两元素的取node.rand操作必定是一致的
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None


def copyList(head):
    if head is None:
        return head 
    
    map_ = {}
    cur = head 
    while head != None:
        map_[head] = Node(head.val)
        head = head.next 
    
    while head != None:
        new_head = Node(head.val)
        new_head.next = map_[head.next] 
        new_head.rand = map_[head.rand]
        head = head.next 
    return new_head 


# 1.在每个节点的后面插入一个相同的节点
# 2.将插入节点设置rand属性
# 3.分离原始节点和插入节点
def copylist2(head):
    if head is None:
        return None

    # 1.增加节点
    cur = head 
    while cur != None:
        node = Node(head.val)
        node.next = cur.next 
        cur.next = node
        cur = cur.next.next

    # 2.添加rand属性
    cur = head 
    while cur != None:
        node = cur.next 
        node.rand = node.rand.next 
        cur = cur.next.next 

    # 3.分离节点
    copy_head = head.next   # 记录新链表的头节点
    cur = head 
    while cur != None:
        next = cur.next.next 
        copy_node = cur.next   # 遍历记录新链表的节点
        cur.next = next 
        copy_node.next = next.next if next != None else None   # 如果next的下一个节点存在说明copy_node的下一个节点也存在
        cur = next 
    return copy_head 



