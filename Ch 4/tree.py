# CTCI Chapter 4

from node import Node

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, node):
        if self.root is None:
            self.root = Node(data)
        else:
            if (data < node.data):
                if (node.left != None):
                    self.insert(data, node.left)
                else:
                    node.left = Node(data)
            else:
                if (node.right != None):
                    self.insert(data, node.right)
                else:
                    node.right = Node(data)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def preorder(self, node):
        if not node:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    def delete(self, data, node):
        if not node:
            return node

        if node.data > data:
            node.left = self.delete(data, node.left)
        elif node.data < data:
            node.right = self.delete(data, node.right)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            temp = node.right
            min = temp.data
            while temp.left:
                temp = temp.left
                min = temp.data
            node.data = min
            node.right = self.delete(node.data, node.right)
        return node
