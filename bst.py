from linked_list import Doubly_LinkedList
# implementation of a BT(Binary Tree)
# A Binary Tree Data Structure is a hierarchial data structure
# in which each node has at most two children,
# reffered to as the left child and the right child.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
        self.dl = Doubly_LinkedList()
    def insert(self, root, value):
        if root is None:
            return Node(value)
        
        
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        self.dl.append(value)

        


        return root
    
    def insert_root(self, value):
        # def insert(self, root, value): # trying out nested functions :)
        #     if root is None:
        #         return Node(value)
        #     if value < root.value:
        #         root.left = self.insert(root.left, value)
        #     else:
        #         root.right = self.insert(root.right, value)
        #     self.dl.append(value)
        #     return root
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self.insert(self.root, value)
    def findMin(self, root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root.value
    def findMax(self, root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root.value
    def contains(self, root, value):
        if root is None:
            return False
        if value == root.value:
            return True
        if value < root.value:
            return self.contains(root.left, value)
        return self.contains(root.right, value)
    def delete(self, root, value):
        if root is None:
            return Node(value)
        
        
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        self.dl.delete(value)
        
    def print(self, root):
        if root is None:
            return
        self.print(root.left)
        print(root.value)
        self.print(root.right)
bst = BST()
bst.insert_root(5)
bst.insert_root(3)
bst.insert_root(7)
bst.insert_root(2)
bst.delete(bst.root, 3)

print("BST Inorder Traversal:")
bst.print(bst.root)
print("\nDoubly Linked List:")

print("\nMin Value:", bst.findMin(bst.root))
print("Max Value:", bst.findMax(bst.root))


print("\nContains 3:", bst.contains(bst.root, 3))
print("Contains 8:", bst.contains(bst.root, 8))
