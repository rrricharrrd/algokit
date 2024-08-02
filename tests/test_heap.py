import pytest

from data_structures import Heap, HeapError


def test_empty():
    heap = Heap()
    assert heap.is_empty()
    assert len(heap) == 0
    print(heap)


def test_errors():
    heap = Heap()
    with pytest.raises(HeapError):
        heap.peek()


def test_heap():
    heap = Heap()
    heap.insert(1)
    heap.insert(3)
    heap.insert(2)
    print(heap)
    assert len(heap) == 3


def test_heap_walk():
    items = [5, 3, 4, 2, 1]
    heap = Heap.heapify(items)
    heap_items = []
    while not heap.is_empty():
        minimum = heap.extract_min()
        heap_items.append(minimum)
    assert heap_items == sorted(items)
