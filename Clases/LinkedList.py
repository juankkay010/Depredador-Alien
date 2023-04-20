from .Node import *


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)



