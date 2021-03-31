class Queue:
    DEFAULT_SIZE = 10

    def __init__(self):
        self.arr = [None] * 10
        self.size = 0
        self.front = 0
    

    def __len__(self):
        return self.size
    

    def is_empty(self):
        return self.size== 0
    

    def get_first(self):
        if self.is_empty():
            return None
        return self.arr[self.front]
    

    def enqueue(self, item):
        if self.size == len(self.arr):
            self.resize(2 * self.size)
        self.arr.append(item)
        self.size += 1

    
    def dequeue(self):
        if self.is_empty():          
            return None
        item = self.arr[self.front]
        self.arr[self.front] = None
        self.front += 1
        self.size -= 1
        return item


    def resize(self, new_size):
        old = self.arr
        self.arr = [None] * new_size
        for i in range(self.size):
            self.arr[i] = old[i]
        self.front = 0
        
    
    def print_queue(self):
        for i in range(self.size):
            print(self.arr[i], end=' ')
    
    

        

         


