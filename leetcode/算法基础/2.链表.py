# 1.反转单向链表
def reserve_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

# 2.反转双向链表
def reserve_double_list(head):
    pre = None
    next = None
    while head is not None:
        next = head.next
        head.next = pre
        head.last = next  # 多一步，同时调整last节点
        pre = head
        head = next
    return pre


# 3. 删除链表中所有为num的节点
def delete_list_node(head, num):
    while head is not None:
        if(head.val != num):
            break
        head = head.next
    # 此时head来到第一个不是num的位置，考虑前n个节点都是num的情况
    pre = head
    cur = head
    while cur is not None:
        if cur.val == num:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return head




# 4. 利用两个栈实现pop， push，getMin的侧重都是O（1）
class TwoStack:
    def __init__(self):
        self.data_ = []  # 存放数据
        self.min_ = []   # 存放最小值
    
    def push(self, item):
        self.data_.append(item)
        if len(self.min_) == 0:
            self.min_.append(item)
        else:
            if item <= self.min_[-1]:
                self.min_.append(item)
            else:
                self.min_.append(self.min_[-1])
    
    def pop(self):
        if len(self.data_) != 0:
            self.data_.pop()
            self.min_.pop()
    
    def get_min(self):
        return self.min_[-1]


# 5. 两个队列完成栈
# 思路:queue只能pop(0), push操作时：轮流使用两个栈，空栈用来添加新元素，将另一个非空栈的元素全部依次pop(0)到这个栈中
#     pop操作时，弹出非空栈的元素即可
class TwoQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self, item):
        if len(self.queue1) == 0:
            self.queue1.append(item)
        elif len(self.queue2) == 0:
            self.queue2.append(item)

        if len(self.queue1) == 1 and len(self.queue2) >= 1:
            while len(self.queue2) > 0:
                self.queue1.append(self.queue2.pop(0))
        elif len(self.queue2) == 1 and len(self.queue1) >= 1:
            while len(self.queue1) > 0:
                self.queue2.append(self.queue1.pop(0))
    
    def pop(self):
        if len(self.queue1) != 0:
            return self.queue1.pop(0)
        elif len(self.queue2) != 0:
            return self.queue2.pop(0)
        return None


# 6.两个栈完成队列
class TwoStack:
    def __init__(self):
        self.accept = []   # 接收数据
        self.output = []   # 弹出数据
    
    def push(self, item):
        self.accept.append(item)
    
    def pop(self):
        if self.output == []:
            while self.accept != []:
                self.output.append(self.accept.pop())
        if self.output != []:
            return self.output.pop()
        else:
            return None

    

# master公式
# T(n) = a * T(n/b) + O(n^d), a,b, d都是常数的递归函数，可以master确定时间复杂度
# 1. log(b, a) > d, 复杂度O(N^log(b, a))
# 2. log(b, a) < d, 复杂度O(N^d)
# 3. log(b, a) == d, 复杂度O(N^d * log(n))

 

# 哈希表：增删改查都是O（1）


# 判断链表是不是回文结构
# 思路：利用一个栈，将链表从头节点开始依次压入栈中，然后依次遍历链表，栈也依次弹出元素进行比较
# 优化空间方法： 利用快慢指针，慢指针停止的时候将后半段加入栈中，然后利用后半段来和前半段进行比较，可以省一半的空间
def is_list_huiwen(head):
    if head.next is not None and head.next.next is None:
        return True
    stack = []
    cur = head.next
    while cur is not None:
        stack.append(cur)
        cur = cur.next
    while head.next is not None:
        if head.next.val != stack.pop().val:
            return False
        head = head.next
    return True

    


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
        

