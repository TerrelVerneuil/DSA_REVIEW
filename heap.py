# A Heap is a complete binary tree data structure 
# that satisfies the heap property: for every node, 
# the value of its children is greater than or equal 
# to its own value. Heaps are usually used to 
# implement priority queues, where the smallest 
# (or largest) element is always at the root of the tree.

# Binary Heap is a complete binary tree that satisfies the heap property.
class Min_Heap:
    def __init__(self):
        self.heap = []
    def getMin(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    def extractMin(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)     
        return min_value
    def decreaseKey(self, index, value):
        if index < 0 or index >= len(self.heap):
            return None
        self.heap[index] = value
        self.bubble_up(index) 
    def insert(self, value):
        self.heap.append(value) #added at end of heap
        self.bubble_up(len(self.heap) - 1)
    def delete(self, index):
        if index < 0 or index >= len(self.heap):
            return None
        self.heap[index] = self.heap.pop()
        if index < len(self.heap):
            self.bubble_down(index)
    # bubble up is used to maintain the heap property after inserting a new element
    def bubble_down(self, index):
        if index < 0 or index >= len(self.heap):
            return None
        
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[index]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[index]:
           smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.bubble_down(smallest)
    def bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
class Max_Heap:
    def __init__(self):
        self.heap = []
    def getMax(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    def extractMax(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)     
        return max_value
    def increaseKey(self, index, value):
        if index < 0 or index >= len(self.heap):
            return None
        self.heap[index] = value
        self.bubble_up(index) 
    def insert(self, value):
        self.heap.append(value) #added at end of heap
        self.bubble_up(len(self.heap) - 1)
    def delete(self, index):
        if index < 0 or index >= len(self.heap):
            return None
        self.heap[index] = self.heap.pop()
        if index < len(self.heap):
            self.bubble_down(index)
    def bubble_down(self, index):
        if index < 0 or index >= len(self.heap):
            return None
        
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[index]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[index]:
           largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.bubble_down(largest)
    def bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

min_heap = Min_Heap()
max_heap = Max_Heap()
for i in [10, 20, 5, 15, 30]:
    min_heap.insert(i)
    max_heap.insert(i)

min_heap.delete(1)
print(min_heap.heap)
print(max_heap.heap)
