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
        self.prev = None
class Singly_LinkedList():
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
            if self.tail is None:
                self.tail = self.head
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
        current = self.head
        index = 0
        while current:
            if current.value == value:
                print(index) # value is found
                return True
            else:
                index += 1 # increment index if value found
                current = current.next
        # print(index)
        if(index >= self.size): # value not found
            print("value not found")
        else:
            print(index)
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
            if self.head is None:
                self.tail = None
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
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
    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head  
            self.head.prev = node
            self.head = node  
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
        current = self.head
        index = 0
        while current:
            if current.value == value:
                print(index) # value is found
                return True
            else:
                index += 1 # increment index if value found
                current = current.next
        # print(index)
        if(index >= self.size): # value not found
            print("value not found")
        else:
            print(index)
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

# Singly_LinkedList = Singly_LinkedList()
# Singly_LinkedList.insert(1, 0)
# Singly_LinkedList.insert(2, 1)

# Singly_LinkedList.append(2)
# Singly_LinkedList.append(3)
# Singly_LinkedList.delete(3)
# Singly_LinkedList.append(4)
# Singly_LinkedList.traverse()


# dl = Doubly_LinkedList()
# dl.append(1)
# dl.append(2)
# dl.traverse()
# dl.search(1)
# print(Singly_LinkedList.size())