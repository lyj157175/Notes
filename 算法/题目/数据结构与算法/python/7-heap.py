class Heap:

    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def add(self, item):
        self.data.append(item)
        self.upheap(len(self.data)-1)
    
    def get_max(self):
        if self.is_empty():
            return None
        return self.data[0]
    
    def remove_min(self):
        if self.is_empty():
            return None
        self.swap(0, len(self.data)-1)
        item = self.data.pop()
        self.downheap(0)
        return item
    
    def _parent(self, idx):
        return (idx-1) // 2
    
    def _left(self, idx):
        return (2*idx) + 1
    
    def _right(self, idx):
        return (2*idx) + 2
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def upheap(self, idx):
        parent = (idx-1) // 2
        if idx > 0 and self.data[idx] > self.data[parent]:
            self.swap(idx, parent)
            self.upheap(parent)
        
    def downheap(self, idx):
        left = 2*idx + 1
        right = 2*idx + 2
        if left < len(self.data) and self.data[left] > self.data[idx]:  # 左节点存在
            large = left
        if right < len(self.data) and self.data[right] > self.data[large]: # 右节点存在
                large = right
        if large != idx:
            self.swap(large, idx)
            self.downheap(large)
    


# 堆排序
def heapify(arr, heap_size, idx):
    '''对idx个节点进行heapify, 大顶堆'''
    left = 2*idx + 1
    right = 2*idx + 2
    large = idx
    if left < heap_size and arr[left] > arr[idx]:  # 存在左节点
        large = left
    if right < heap_size and arr[right] > arr[large]:   # 存在右节点
        large = right
    if large != idx:
        arr[large], arr[idx] = arr[idx], arr[large]
        heapify(arr, heap_size, large)


def build_heap(arr):
    '''从最后一个节点的父节点开始,只到根节点'''
    heap_size = len(arr)
    for i in range((heap_size-2)//2, -1, -1):   
        heapify(arr, heap_size, i)

def heap_sort(arr):
    build_heap(arr)  # 构建大顶堆
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 交换第一个和最后一个节点，最大值换到最后
        heapify(arr, i, 0)
    return arr


if __name__ =='__main__':
    arr = [3, 6, 8, 1, 2, 3, 9, 0, 12, 7]
    print(heap_sort(arr))


