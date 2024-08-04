from interviews.data_structures._priority_queue import PriorityQueue


def test_empty():
    queue = PriorityQueue()
    assert queue.is_empty()
    assert len(queue) == 0


def test_enqueue():
    queue = PriorityQueue()
    queue.enqueue(1, priority=3)
    queue.enqueue(2, priority=1)
    queue.enqueue(3, priority=2)
    queue.enqueue(4, priority=2)
    assert len(queue) == 4
    assert queue.peek() == 2


def test_dequeue():
    queue = PriorityQueue()
    queue.enqueue(1, priority=3)
    queue.enqueue(2, priority=1)
    queue.enqueue(3, priority=2)
    queue.enqueue(4, priority=2)

    item = queue.dequeue()
    assert item == 2
    item1 = queue.dequeue()
    item2 = queue.dequeue()
    assert {item1, item2} == {3, 4}
    item = queue.dequeue()
    assert item == 1


def test_change_priority():
    queue = PriorityQueue()
    item1 = queue.enqueue(1, priority=3)
    item2 = queue.enqueue(2, priority=1)
    queue.enqueue(3, priority=2)

    queue.change_priority(item2, priority=4)
    queue.change_priority(item1, priority=1)

    item = queue.dequeue()
    assert item == 1
    item = queue.dequeue()
    assert item == 3
    item = queue.dequeue()
    assert item == 2
