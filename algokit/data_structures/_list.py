from ._exception import DataStructureException


class LinkedListError(DataStructureException):
    pass


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"ListNode<{self.data}>"


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ""
        for node in self:
            if s:
                s += "->"
            s += f"[{node.data}]"
        return f"LinkedList<{s}>"

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

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
            for n in self:
                pass
            n.next = node

    def delete(self, data):
        if self.head is None:
            raise LinkedListError("Empty list")

        if self.head.data == data:
            self.head = self.head.next
            return data

        found = False
        prev = None
        for node in self:
            if node.data == data:
                found = True
                break
            prev = node

        if found:
            prev.next = node.next
        else:
            raise LinkedListError(f"Element {data} could not be found")
        return data
