'''编写一个类，用两个栈实现对列，支持队列的基本操作（add.poll,peek）'''


class MyQueue:

    def __init__(self,):
        self.in_ = []    # 进元素
        self.out_ = []   # 出元素
    
    def add(self, item):
        self.in_.append(item)
    
    def poll(self):
        if len(self.out_) ==0:
            if len(self.in_) == 0:
                return None
            while len(self.in_) !=0:
                self.out_.append(self.in_.pop())
        return self.out_.pop()
    
    def peek(self):
        if len(self.out_) ==0:
            if len(self.in_) == 0:
                return None
            while len(self.in_) !=0:
                self.out_.append(self.in_.pop())
        return self.out_[-1]
        
            
            
