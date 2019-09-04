# CTCI Chapter 4

from tree import Tree
from node import Node

def main():
    t = Tree()
    rt = Node(3)
    t.root = rt
    t.insert(7, rt)
    t.insert(1, rt)
    t.insert(5, rt)
    t.preorder(rt)
    t.delete(3, rt)
    print("------------")
    t.preorder(rt)
main()
