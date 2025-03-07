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
        if position > self.size:
            print("err -> position out of range")
        node = Node(value)
        if position == 0: # at head position
            node.next = self.head
            self.head = node
            if not self.tail:
                self.tail = node
            
        elif position == self.size: # at tail position  
            
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
        else: # at any other position
            current = self.head
            #traverse
            for _ in range(position - 1):
                current = current.next
           
            node.next = current.next
            current.next = node
        self.size += 1      
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
    def append(self, value): # add to the end of the list
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def prepend(self, value): # add to the beginning of the list
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
                print(f"Value found at -> {index}") # value is found
                return True
            else:
                index += 1 # increment index if value found
                current = current.next
        # print(index)
        if(index >= self.size): # value not found
            print("err -> Value not found")
        else:
            print(f"Value found at - {index}")
        return False
    def insert(self, value, position):
        if position > self.size:
            print("err -> position out of range")
        node = Node(value)
        if position == 0: # at head position
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if not self.tail:
                self.tail = node
            
            
            
            
        elif position == self.size: # at tail position  
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
        else: # at any other position
            current = self.head
            #traverse
            for _ in range(position - 1):
                current = current.next
            node.next = current.next
            node.prev = curerent
            
            if current.next:
                current.next.prev = node
            current.next = node
        self.size += 1
        
            
            
            # node.prev = current
    def delete(self, value):
        if self.head is None:
            return
        
        if self.head.value == value: #removes from the beginning of the list
            self.head = self.head.next
            self.head.prev = None
            if self.head is None:
                self.tail = None
            return
        current = self.head
        
        
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                # current.next.prev = current
                return
            current = current.next
            

Singly_LinkedList = Singly_LinkedList()
Singly_LinkedList.insert(1, 0)
# singly_linked_list = Singly_LinkedList()
Singly_LinkedList.insert(1, 0)
# Singly_LinkedList.insert(2, 5)

Singly_LinkedList.append(2)
Singly_LinkedList.append(3)
Singly_LinkedList.delete(3)
Singly_LinkedList.append(4)
Singly_LinkedList.delete(4)
Singly_LinkedList.traverse()


# dl = Doubly_LinkedList()
# dl.append(1)
# dl.append(2)
# dl.append(3)
# dl.delete(1)
# dl.delete(2)
# dl.insert(5,4)
# dl.insert(5,4)
# print(dl)
# dl.traverse()
# dl.search(1)
# dl.search(2)
# dl.search(3)
# dl.search(4)

# dl.delete(1)


# dl.traverse()

# print(Singly_LinkedList.size())