import pytest

from interviews.data_structures import Queue, QueueError


def test_empty():
    queue = Queue()
    assert queue.is_empty()
    assert len(queue) == 0
    print(queue)


def test_errors():
    queue = Queue()
    with pytest.raises(QueueError):
        queue.peek()
    with pytest.raises(QueueError):
        queue.remove()


def test_queue():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.remove()
    assert len(queue) == 2
    print(queue)
