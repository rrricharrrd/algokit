from data_structures import Stack


def test_empty():
    stack = Stack()
    assert stack.is_empty()
    print(stack)


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print(stack)
