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

    def palindrome(self):
        curr = self.head
        prev = self.head

        while curr != self.tail and prev:
            if prev.next == self.tail:
                if curr.data != prev.next.data:
                    return False
                self.tail = prev
                curr = curr.next
                prev = curr
            else:
                prev = prev.next

        return True

    def removeDupes(self):
        temp = self.head
        prevSize = 0
        currSize = 0
        dupes = set()
        while temp:
            if temp.data in dupes:
                self.remove(temp.data)
            else:
                dupes.add(temp.data)
            temp = temp.next

    def toLast(self, k):
        len = 0
        kth = 0
        temp = self.head

        while temp:
            len += 1
            temp = temp.next

        temp = self.head

        if len < k or k < 1:
            return -1
        else:
            while temp:
                kth += 1
                if kth == (len-k+1):
                    return temp.data
                temp = temp.next
            return -1

    def printLL(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
