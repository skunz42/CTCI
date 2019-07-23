# CTCI Ch 2

from node import Node
from LLC import LLC

def main():
    l = LLC()
    l.insert(2)
    #l.insert(4)
    #l.insert(4)
    #l.insert(2)
    l.printLL()
    #l.remove(2)
    #l.remove(3)
    print('-----------------')
    print(l.palindrome())
    #l.printLL()
main()
