"""
问题描述：一个栈中元素的类型为整型，现在想将该栈从顶到底按从大到小的顺序排序，只许
额外申请一个栈。除此之外，可以申请新的变量，但不能申请额外的数据结构。如何完成排序？

思路：将要排序的栈记为stack，申请的辅助栈记为help。在stack上执行pop操作，弹出的
元素记为cur.
1)如果cur小于或等于help的栈顶元素，则将cur直接压入help
2)如果cur大于help的栈顶元素，则将help的元素逐一弹出，逐一压入stack，直到cur小于
或等于help的栈顶元素，再将cur压入help
3)将help的所有元素压入stack
"""

def sort_stack(stack):
    help_ = []
    while len(stack)!=0:
        cur = stack.pop()
        while len(help_) !=0 and cur > help_[-1]:
            stack.append(help_.pop())
        help_.append(cur)
    while len(help_) != 0:
        stack.append(help_.pop())
    return stack
        


print(sort_stack([3,2,1,5,4]))