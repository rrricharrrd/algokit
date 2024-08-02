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
        s = ""
        n = self.head
        while n is not None:
            if s:
                s += "->"
            s += f"[{n.data}]"
            n = n.next
        return f"LinkedList<{s}>"

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
            return data

        found = False
        prev = None
        while n is not None:
            if n.data == data:
                found = True
                break
            prev = n
            n = n.next

        if found:
            prev.next = n.next
        else:
            raise LinkedListError("Element could not be found")  # TODO
        return data
