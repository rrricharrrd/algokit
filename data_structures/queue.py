class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        node = Node(item)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next  # TODO null
        return data

    def peek(self):
        return self.head

    def is_empty(self):
        return self.head is not None

    def print(self):
        str = ""
        n = self.head
        while n is not None:
            if str:
                str += "->"
            str += f"[{n.data}]"
            n = n.next
        return str


if __name__ == "__main__":

    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.remove()
    print(q.print())
