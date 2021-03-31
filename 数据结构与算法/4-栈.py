class Stack:

    def __init__(self):
        self.arr = []
    
    def __len__(self):
        return len(self.arr)
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def push(self, item):
        self.arr.append(item)
    
    def top(self):
        if self.is_empty:
            return None
        return self.arr[-1]

    def pop(self):
        if self.is_empty:
            return None
        return self.arr.pop()
    
    def print_stack(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=' ')
    
    