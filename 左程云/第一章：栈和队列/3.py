"""
一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。将这个栈
转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，要求
只能用递归函数来实现，不能使用其他数据结构，

思路：首先使用一个递归函数获取到栈底元素，再构造另外一个递归函数来进行reverse操作
"""

# 每次得到栈底元素并将其从栈底删除
def get_and_remove_last(stack):
    result = stack.pop()
    if len(stack)==0:
        return result
    else:
        last = get_and_remove_last(stack)
        stack.append(result)
        return last


# 反转栈元素
def reverse(stack):
    if len(stack) == 0:
        return 
    i = get_and_remove_last(stack)
    reverse(stack)
    stack.append(i)
    return stack
    

if __name__ == "__main__":
    print(reverse([1,2,3,4,5]))
