"""
问题描述：给定一个单向链表的头结点head，节点的值类型是整型，再给定一个
整数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于pivot
的节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点，除
这个要求外，对调整后的节点顺序没有更多的要求

例如：链表 9->0->4->5->1,pivot=3
调整后的链表可以是1->0->4->9->5,也可以是0->1->9->5->4,中间部分都是
等于3的节点（本例中这个部分为空），右部分都是大于3的节点即可。对某部分内
部的节点顺序不作要求。

进阶：
在原问题的要求之上再增加两个要求：
1）在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左到右的顺
序与原链表中节点的先后次序一致,比如9->0->4->5->1,pivot=3，那么调整后
链表为0->1->9->4->5
2）如果链表的长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

# 将节点依次加入到数组中，对数组中的节点进行快速部分排序，然后将排序的节点依次连接即可
def partionSort(res, pivot):
    left = -1
    right = len(res)
    index = 0   # 记录当前位置

    while index < right:
        if res[index].val < pivot:
            left += 1
            res[left], res[index] = res[index], res[left]
            index += 1
        elif res[index] > pivot:
            right -= 1
            res[right], res[index] = res[index], res[right]
        else:
            index += 1


def partion(head, pivot):
    if  head is None or head.next is None:
        return head 
    
    n = 0
    cur = head 
    while cur != None:
        n += 1
        cur = cur.next 
    
    res = []
    cur = head 
    while cur != None:
        res.append(cur)
        cur = cur.next 
    
    partionSort(res, pivot)  # 将节点进行部分排序
    for i in range(n - 1):
        res[i].next = res[i + 1]
    res[n].next = None
    return res[0]


