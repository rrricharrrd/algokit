import pytest

from interviews.data_structures import Heap, HeapError, PriorityQueue


def test_empty():
    heap = Heap()
    assert heap.is_empty()
    assert len(heap) == 0
    print(heap)

    with pytest.raises(HeapError):
        heap.peek()


def test_heapify():
    heap = Heap.heapify([2, 3, 1])
    assert len(heap) == 3
    assert heap.peek() == 1


def test_insert():
    heap = Heap()
    heap.insert(2)
    heap.insert(3)
    heap.insert(1)
    assert len(heap) == 3
    assert heap.peek() == 1


def test_extract_min():
    items = [5, 3, 4, 2, 1]
    heap = Heap.heapify(items)
    heap_items = []
    while not heap.is_empty():
        minimum = heap.extract_min()
        heap_items.append(minimum)
    assert heap_items == sorted(items)

    with pytest.raises(HeapError):
        heap.extract_min()


def test_str():
    heap = Heap()
    print(heap)

    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    print(heap)


def test_priority_queue():
    queue = PriorityQueue()
    queue.enqueue(1, priority=1)
    queue.enqueue(2, priority=3)
    queue.enqueue(3, priority=2)
    queue.enqueue(4, priority=2)

    item = queue.dequeue()
    assert item == 2
    item1 = queue.dequeue()
    item2 = queue.dequeue()
    assert {item1, item2} == {3, 4}
    item = queue.dequeue()
    assert item == 1
