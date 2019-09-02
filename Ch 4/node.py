# CTCI Chapter 4

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data, root):
        if root is None:
            root = Node(data)
        else:
            if (data < root.data):
                if (root.left != None):
                    self.insert(data, root.left)
                else:
                    root.left = Node(data)
            else:
                if (root.right != None):
                    self.insert(data, root.right)
                else:
                    root.right = Node(data)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return
        print(root.data)
        self.postorder(root.left)
        self.postorder(root.right)
