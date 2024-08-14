from algokit.data_structures._priority_queue import PriorityQueue, PriorityQueueEntry


def test_empty():
    queue = PriorityQueue()
    assert queue.is_empty()
    assert len(queue) == 0


def test_enqueue():
    queue = PriorityQueue()
    queue.enqueue(1, priority=3)
    item2 = queue.enqueue(2, priority=1)
    queue.enqueue(3, priority=2)
    queue.enqueue(4, priority=2)
    assert len(queue) == 4
    assert queue.peek() == item2
    assert isinstance(item2, PriorityQueueEntry)
    assert item2.data == 2
    assert item2.priority == 1


def test_dequeue():
    queue = PriorityQueue()
    add1 = queue.enqueue(1, priority=3)
    add2 = queue.enqueue(2, priority=1)
    add3 = queue.enqueue(3, priority=2)
    add4 = queue.enqueue(4, priority=2)

    item = queue.dequeue()
    assert item == add2
    item1 = queue.dequeue()
    item2 = queue.dequeue()
    assert {item1, item2} == {add3, add4}
    item = queue.dequeue()
    assert item == add1


def test_change_priority():
    queue = PriorityQueue()
    item1 = queue.enqueue(1, priority=3)
    item2 = queue.enqueue(2, priority=1)
    item3 = queue.enqueue(3, priority=2)

    queue.change_priority(item2, priority=4)
    queue.change_priority(item1, priority=1)

    item = queue.dequeue()
    assert item == item1
    item = queue.dequeue()
    assert item == item3
    item = queue.dequeue()
    assert item == item2
