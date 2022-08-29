# 动态数组实现

class DynamicArray:

    def __init__(self):
        self.n = 0
        self.size = 10  # 数组容量
        self.arr = []
    
    def __len__(self):
        return len(self.n)
    
    def is_empty(self):
        return self.n == 0
    
    def getitem(self, idx):
        if idx < 0 or idx > len(self.n):
            return None
        else:
            return self.arr[idx]
    
    def resize(self, new_size):
        new_arr = []
        for i in range(len(self.n)):
            new_arr[i] = self.arr[i]
        self.size = new_size
        self.arr = new_arr
    
    def append(self, item):
        if self.n == self.size:
            self.resize(2*self.size)
        self.arr[self.n] = item
        self.n += 1
        
    
    def insert(self, pos, item):
        if self.n == self.size:
            self.resize(2*self.size)
        for i in range(self.n, pos, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[pos] = item
        self.n += 1

    
    def remove(self, item):
        for i in range(self.n):
            if self.arr[i] == item:
                for j in range(i, self.n-1):
                    self.arr[j] == self.arr[j+1]
                self.arr[self.n-1] = None
                self.n -= 1
                return 
        return None
        

    def print_(self):
        for i in range(self.n):
            print(self.arr[i], end='')
        print()



