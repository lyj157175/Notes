class Node:
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None
    

class LikedList:

    def __init__(self):
        self.head = Node()
        self.tail = None
        self.length = 0
    

    def peek(self):
        if self.head.next is None:
            return None
        return self.head.next
    

    def get_first(self):
        if self.head.next is None:
            return None
        return self.head.next
    

    def get_last(self):
        if self.head.next is None:
            return None
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur


    def get(self, idx):
        if idx < 0 or idx > self.length:
            return None 
        if self.head.next is None:
            return None
        cur = self.head
        for i in range(idx):
            cur = cur.next
        return cur


    def add_first(self, item):
        node = Node(item)
        if self.head.next is None:
            self.head.next = node
        node.next = self.head.next
        self.head.next = node
        self.length += 1
    

    def add_last(self, item):
        node = Node(item, None)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        self.length += 1

    
    def add(self, idx, item):
        node = Node(item)
        if idx < 0 or idx > self.length:
            return None
        if self.head.next is None:
            if idx == 0:
                self.head.next = node
            else:
                return None
        cur = self.head
        for i in range(idx):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        self.length += 1
    

    def remove_first(self):
        if self.head.next is None:
            return None
        node = self.head.next
        self.head.next = self.head.next.next
        self.length -= 1
        return node.val


    def remove_last(self):
        if self.head.next is None:
            return None
        cur = self.head
        while cur.next.next:
            cur = cur.next
        node = cur.next 
        cur.next = None
        self.length -= 1
        return node.val
    
    def remove(self, idx):
        if idx < 0 or idx > self.length:
            return None
        if self.head.next is None:
            return None
        cur = self.head
        for i in range(idx):
            cur = cur.next
        node = cur.next
        cur.next = cur.next.next
        self.length -= 1
        return node.val
    
    def print_list(self):
        if self.head.next is None:
            return None
        cur = self.head.next
        for i in range(self.length):
            print(cur.val, end=' ')
            cur = cur.next

if __name__ == '__main__':
    linked_list = LikedList()
    for i in range(10):
        linked_list.add_last(i)
    linked_list.print_list()
        
                
    
    

            







