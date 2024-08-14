import pytest

from algokit.data_structures import LinkedList, LinkedListError


def test_empty():
    lst = LinkedList()
    assert lst.is_empty()
    assert len(lst) == 0
    with pytest.raises(LinkedListError):
        lst.peek()
    with pytest.raises(LinkedListError):
        lst.delete(1)


def test_insertion():
    lst = LinkedList()
    assert len(lst) == 0
    lst.append(1)
    assert len(lst) == 1
    lst.append(2)
    assert lst.peek() == 1
    assert len(lst) == 2
    lst.append(3)
    assert len(lst) == 3
    lst.append(1)
    assert len(lst) == 4


def test_deletion():
    lst = LinkedList()
    lst.append(1)
    lst.delete(1)  # delete only element (at head)
    assert lst.is_empty()

    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.delete(3)  # delete from middle
    assert len(lst) == 2
    lst.delete(4)  # delete from tail
    assert len(lst) == 1

    lst.append(2)  # add duplicate
    lst.delete(2)
    assert len(lst) == 1
    lst.delete(2)
    assert len(lst) == 0

    lst.append(1)
    with pytest.raises(LinkedListError):
        lst.delete(99)


def test_str():
    lst = LinkedList()
    print(lst)
    lst.append(1)
    lst.append(2)
    print(lst)
    for node in lst:
        print(node)
