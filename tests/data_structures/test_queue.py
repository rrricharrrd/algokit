import pytest

from algokit.data_structures import Queue, QueueError


def test_empty():
    queue = Queue()
    assert queue.is_empty()
    assert len(queue) == 0

    with pytest.raises(QueueError):
        queue.peek()
    with pytest.raises(QueueError):
        queue.remove()


def test_add():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert len(queue) == 3
    assert queue.peek() == 1


def test_remove():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    item = queue.remove()
    assert item == 1
    assert queue.peek() == 2
    item = queue.remove()
    assert item == 2
    assert queue.peek() == 3
    assert len(queue) == 1


def test_str():
    queue = Queue()
    print(queue)
    queue.add(1)
    queue.add(2)
    print(queue)
    print(queue.head)
