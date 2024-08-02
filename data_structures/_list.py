from ._exception import DataStructureException


class LinkedListError(DataStructureException):
    pass


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
        return f"LinkedList<{str}>"

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            raise LinkedListError("Empty list")

        return self.head.data

    def append(self, data):
        node = ListNode(data)
        n = self.head
        if n is None:
            self.head = node
        else:
            while n.next is not None:
                n = n.next
            n.next = node

    def delete(self, data):
        if self.head is None:
            raise LinkedListError("Empty list")

        n = self.head
        if n.data == data:
            self.head = n.next
            return

        prev = None
        while n is not None:
            if n.data == data:
                break
            n = n.next
            prev = n
        prev.next = n.next
        return
