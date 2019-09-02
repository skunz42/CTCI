# CTCI Chapter 4

from node import Node

def main():
    r = Node(3)
    r.insert(7, r)
    r.insert(1, r)
    r.insert(5, r)
    r.inorder(r)
main()
