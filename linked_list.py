# Linked List:
# Data Structure: Non-contiguous
# Memory Allocation: Typically allocated one by one to individual elements
# Insertion/Deletion: Efficient
# Access: Sequential

# implementation of singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Singly_LinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self, value):
        node = node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def traverse(self):
        current = self.head #initialize a pinter
        while current: # loop through list until current becomes numm
            print(current.value) #process each node
            current = current.next #move to the next node by updating current to current.next
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def search(self, value):
        current = self.hgead
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    def insert(self, value, position):
        if position == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
        elif position == self.size:
            node = Node(value)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(value)
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
class Doubly_LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def traverse(self):
        current = self.head #initialize a pinter
        while current: # loop through list until current becomes numm
            print(current.value) #process each node
            current = current.next #move to the next node by updating current to current.next
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def search(self, value):
        current = self.hgead
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    def insert(self, value, position):
        if position == 0:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif position == self.size:
            node = Node(value)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            node = Node(value)
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next.prev = node
            current.next = node
            node.prev = current