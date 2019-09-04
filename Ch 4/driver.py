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
    '''r = Node(3)
    r.insert(7, r)
    r.insert(1, r)
    r.insert(5, r)
    r.preorder(r)
    r.delete(3, r)
    print("------------")
    r.preorder(r)'''
main()
