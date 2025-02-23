# stacks can enqueue and dequeue in O(1) time
# queues follow the FIFO principle

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
# queues have the ability to
# enqueue and dequeue in O(1) time
# queues can be implemented using arrays or linked lists
# 

class Queue: #constructor class we could make this node based
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def size(self):
        temp = self.front
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def show(self):
        arr_show = []
        temp = self.front
        while temp:  
            arr_show.append(temp.data)
            temp = temp.next
        return arr_show 
    def isEmpty(self):
        if self.front is None:
            return True
        return False
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    def dequeue(self):
            if self.front is None:  
                return None
            temp = self.front  
            self.front = self.front.next  
            if self.front is None:  
                self.rear = None
            return temp.data
       

       
        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
# queue.enqueue(8)
print(queue.show())
print(queue.size())
queue.dequeue()

print(queue.show())
print(queue.peek())
# queue.dequeue()

