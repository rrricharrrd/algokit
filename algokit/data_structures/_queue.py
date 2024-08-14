from ._exception import DataStructureException


class QueueError(DataStructureException):
    pass


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"QueueNode<{self.data}>"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = ""
        n = self.head
        while n is not None:
            if s:
                s += "->"
            s += f"[{n.data}]"
            n = n.next
        return f"Queue<{s}>"

    def __len__(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise QueueError("Empty queue")

        return self.head.data

    def add(self, item):
        node = QueueNode(item)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        if self.is_empty():
            raise QueueError("Empty queue")

        data = self.head.data
        self.head = self.head.next
        return data
