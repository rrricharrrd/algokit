from data_structures import Stack


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s)
