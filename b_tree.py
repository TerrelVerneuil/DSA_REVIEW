# A B-Tree is a type of self balancing search tree that allows each node to store multiple keys making it more efficent for large data sets
# in B-trees nodes can have more than two children

# allows searches, insertiions, sequential access, and deletions in logarithmic time
from linked_list import Doubly_LinkedList

class Node:
    def __init__(self, value=None, max_keys=None, max_children=None):
        self.keys = [value] if value is not None else []
        self.children = []
        
class B_Tree:
    def __init__(self):
        self.root = None
        sorted_root = root.keys.sort()
        self.dl = Doubly_LinkedList()
        max_root = self.root.keys[len(self.root.keys) - 1]
        min_root = self.root.keys[0]
        
    def insert(self, root, value, max_keys, max_children):
        if root is None:
            return Node(value)
        if value < root.keys[0]: #if value is less than the root node smallest key
            root.children[0] = self.insert(root.children[0], value) # becomes leaf node of the smallest key
        if value > root.keys[0]: #if value is greater than the root node smallest key
            root.children[1] = self.insert(root.children[1], value) # becomes leaf node of the largest key
        
            
            
            

        if len(root.children) > max_children:
            root.children = root.children[:max_children]
        if len(root.keys) > max_keys:
            root.keys = root.keys[:max_keys]
        self.dl.append(value)
    
    def delete(self, root, value):
        #first we need to balance the tree to move the value to be deleted to the leaf node
        if root is None:
            return Node(value)
        
        
        if value < root.keys[0]: #if value is less than the root node smallest key
            root.children[0] = self.insert(root.children[0], value) # insert the value in the left child
        if value > root.keys[0]: #if value is greater than the root node smallest key
            root.children[1] = self.insert(root.children[1], value) # insert the value in the right child
        if len(root.children) > max_children:
            root.children = root.children[:max_children]
        if len(root.keys) > max_keys:
            root.keys = root.keys[:max_keys]
        self.dl.delete(value)
        
        
        
    
        