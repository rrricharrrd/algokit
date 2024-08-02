class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def peek(self):
        return self.head.data

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
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s.print())
