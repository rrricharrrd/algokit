import pytest

from algokit.data_structures import Stack, StackError


def test_empty():
    stack = Stack()
    assert stack.is_empty()
    assert len(stack) == 0

    with pytest.raises(StackError):
        stack.peek()
    with pytest.raises(StackError):
        stack.pop()


def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    assert stack.peek() == 3


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    item = stack.pop()
    assert item == 3
    assert stack.peek() == 2
    item = stack.pop()
    assert item == 2
    assert stack.peek() == 1
    assert len(stack) == 1


def test_str():
    stack = Stack()
    print(stack)
    stack.push(1)
    stack.push(2)
    print(stack)
    print(stack.head)
