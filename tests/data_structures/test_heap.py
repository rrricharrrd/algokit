import pytest

from algokit.data_structures import Heap, HeapError


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
