class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1

        return -1

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        i = 0

        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if curr:
            node = Node(val)
            node.next = curr.next
            curr.next = node

    def deleteAtIndex(self, index):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        i = 0

        while curr.next and i < index - 1:
            curr = curr.next
            i += 1

        if curr.next:
            curr.next = curr.next.next