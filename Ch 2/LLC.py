# CTCI Chapter 2

from node import Node

class LLC:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        n = Node(value)

        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def remove(self, value):
        curr = self.head
        prev = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    self.head = curr.next
                    #prev = curr
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next

    def reverse(self):
        prev = None
        while self.head:
            curr = self.head
            self.head = self.head.next
            curr.next = prev
            prev = curr

        self.head = prev

    def printLL(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
