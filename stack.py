# follows the LIFO principle
# stacks can push and pop in O(1) time
# stacks can be implemented using arrays or linked lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
    def pop(self):
        if self.top is None:
            return None
        temp = self.top #store top node
        self.top = self.top.next #move top to the next node
        temp.next = None #remove the link between the top node and the next node
        return temp.data #return the data of the top node
    def size(self):
        temp = self.top
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    def isEmpty(self):
        if self.top is None:
            return True 
    def show(self):
        temp = self.top
        storage = []
        while temp:
            storage.append(temp.data)
            print(temp.data)
            temp = temp.next
        print(f"order representation: {storage}")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
# stack.pop()

print(stack.show())
print(stack.size())

