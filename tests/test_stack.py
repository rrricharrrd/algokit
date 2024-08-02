import pytest

from data_structures import Stack, StackError


def test_empty():
    stack = Stack()
    assert stack.is_empty()
    print(stack)


def test_errors():
    stack = Stack()
    with pytest.raises(StackError):
        stack.pop()


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print(stack)
