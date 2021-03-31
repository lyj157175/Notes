'''用两个栈来实现一个队列，完成队列的Push和Pop操作。队列中的元素为int类型。'''

# 【思路】1号栈push元素，2号栈pop元素。当2号栈为空时将1号栈元素全部依次pop到2中，否则2号栈直接pop

class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return None
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            
        item = self.stack2.pop()
        return item
            


         
        