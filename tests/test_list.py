import pytest

from data_structures import LinkedList, LinkedListError


def test_empty():
    lst = LinkedList()
    assert lst.is_empty()
    assert len(lst) == 0
    print(lst)


def test_errors():
    lst = LinkedList()
    with pytest.raises(LinkedListError):
        lst.peek()
    with pytest.raises(LinkedListError):
        lst.delete(1)


def test_list():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.delete(2)
    print(lst)
    assert len(lst) == 2
