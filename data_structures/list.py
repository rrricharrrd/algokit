class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        n = self.head
        if n is None:
            self.head = node
        else:
            while n.next is not None:
                n = n.next
            n.next = node

    def delete(self, data):
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

    def print(self):
        str = ""
        n = self.head
        while n is not None:
            if str:
                str += "->"
            str += f"[{n.data}]"
            n = n.next
        return str
