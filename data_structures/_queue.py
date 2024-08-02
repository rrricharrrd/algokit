from ._exception import DataStructureException


class QueueError(DataStructureException):
    pass


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def peek(self):
        return self.head

    def is_empty(self):
        return self.head is None

    def __str__(self):
        str = ""
        n = self.head
        while n is not None:
            if str:
                str += "->"
            str += f"[{n.data}]"
            n = n.next
        return f"Queue<{str}>"
