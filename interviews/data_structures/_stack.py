from ._exception import DataStructureException


class StackError(DataStructureException):
    pass


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        str = ""
        n = self.head
        while n is not None:
            if str:
                str += "->"
            str += f"[{n.data}]"
            n = n.next
        return f"Stack<{str}>"

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
            raise StackError("Empty stack")

        return self.head.data

    def pop(self):
        if self.head is None:
            raise StackError("EmptyStack")

        data = self.head.data
        self.head = self.head.next
        return data

    def push(self, item):
        node = StackNode(item)
        node.next = self.head
        self.head = node
