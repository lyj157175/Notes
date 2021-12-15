"""
问题描述：构造一个特殊的栈，可以实现栈的基本功能，并具有实现返回最小值的操作
1）使之pop()、push()和getMin() (求最小值) 的操作的时间复杂度都为O(1)
2）可以使用现成的栈类型

思路：使用两个栈，一个栈保存所有数据，一个栈保存当前最小数据
"""

class MyStack:
    def __init__(self):
        self.data = []
        self.min_ = []
    
    def push(self, item):
        self.data.append(item)
        if len(self.min_) == 0 or item <= self.min_[-1]:
            self.min_.append(item)
        else:
            self.min_.append(self.min_[-1])
    
    def pop(self):
        if len(self.data) == 0:
            return None
        self.min_.pop()
        return self.data.pop()
    
    def getMin(self):
        if len(self.min_) == 0:
            return None
        return self.min_[-1]



