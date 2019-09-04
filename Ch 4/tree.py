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

    '''def delete(self, data, root):
        if not root:
            return root

        if data == root.data and root.left:
            print("g: " + str(self.data))
            self = self.left
            print("g: " + str(self.data))
            return root.left
        elif data == root.data and root.right:
            return root.right

        if root.data > data:
            root.left = self.delete(data, root.left)
        elif root.data < data:
            root.right = self.delete(data, root.right)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            temp = root.right
            min = temp.data
            while temp.left:
                temp = temp.left
                min = temp.data
            root.data = min
            root.right = self.delete(root.right, root.data)
        return root'''
