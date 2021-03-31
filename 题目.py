# 【1】栈和队列---设计一个有getMin功能的栈
# 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
# 【要求】
# 1. pop、push、getMin操作的时间复杂度都是O(1)。
# 2. 设计的栈类型可以使用现成的栈结构
class getMin:
    def __init__(self):
        self.stack_data = []
        self.stack_min = []
    
    def push(self, item):
        self.stack_data.append(item)
        if len(self.getMin()) == 0 or item <= self.getMin():
            self.stack_min.append(item)
    
    def pop(self):
        if len(self.stack_data) == 0:
            raise Exception('stack is empty')
        value = self.stack_data.pop()
        if self.stack_min() == value:
            self.stack_min.pop()
        return value
   
    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception('stack is empty')
        return self.stack_min[-1]
        
            
# 【2】编写一个类，用两个栈实现队列，支持队列的基本操作(add, poll, peek)。
# 　　使用两个栈stackpush、stackpop
#     stackpush栈负责压入数据、stackpop栈负责将stackpush中的元素逆序，用于获取或者弹出栈顶元素。
#     但是有一个规则：stackpop只有为空的时候才再次向stackpush栈索要元素，而且，必须一次拿走stackpush中当前的所有元素。
class queue:
    def __init__(self):
        self.stack_push = []   # 进队列
        self.stack_pop = []    # 出队列
    
    def add(self, item):
        self.stack_push.append(item)
        
    def poll(self):
        if not self.stack_pop() and not self.stack_push():
            raise Exception('queue is empty')
        if len(self.stack_pop) == 0:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()
    
               
    def peek(self):
        if not self.stack_pop() and not self.stack_push():
            raise Exception('queue is empty')
        if len(self.stack_pop) == 0:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]

    
    
# 链表问题
#  给定两个有序链表的头指针head1和head2，打印两个链表的公共部分。
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
def print_common_part(head1, head2):
    if head1 is None or head2 is None:
        return None
    print('common part:', end=' ')
    while head1 or head2:
        if head1.val < head2.val:
            head1 = head1.next
        elif head1.val > head2.next:
            head2 = head2.next
        else:
            print(head1.val, end=' ')
            head1 = head1.next
            head2 = head2.next       
    print()



# 在单链表和双链表中删除倒数第K个节点
# k > 链表长度
# k == 链表长度
# k < 链表长度
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
# 单链表
def removeLastkNode(head, k):
    if head == None or k < 1:
        return head
    fast = slow = head
    while k > 0:
        k -= 1
        if fast == None:
            return head
        else:
            fast = fast.next
    if fast.next == None:
        return head.next
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
            
# 双链表
class DoubleNode:
    def __init__(self, val=None):
        self.val = val
        self.pre = None
        self.next = None
        
def removeLastKDoubleNode(head, k):
    if head == None or k < 1:
        return head
    fast = slow = head
    while k > 0:
        k -= 1
        if fast != None:
            fast = fast.next
        else:
            return head
    if fast == None:
        head = head.next
        head.pre = None
    else:
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        if slow.next != None:
            slow.next.pre = slow
    return head



# 删除中间节点和删除a/b处的节点
def removeMiddle(head):
    # 0,1个节点的情况
    if head == None or head.next == None:
        return head
    # 2个节点的情况,删除第一个点
    if head.next.next == None:
        return head.next
    slow = head
    fast = head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # 删除中间节点
    slow.next = slow.next.next
    return head
        

# 反转单向和双向链表
def reverseList(head):
    if head is None:
        return 
    pre = None
    while head:
        next_ = head.next
        head.next = pre
        pre = head
        head = next_
    return pre
    

# 反转双向链表
def reverseDoubleList(head):
    if head is None:
        return
    pre = None
    while head:
        next_ = head.next
        head.next = pre
        head.pre = next_
        pre = head
        head = next_
    return pre
        
    
# 反转部分链表

def reverse_part_list(head, start, end):
    if head == None or head.next == None:
        return head
    
    
    

    
    
    
    


