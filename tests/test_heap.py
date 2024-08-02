import pytest

from data_structures import Heap, HeapError


def test_empty():
    heap = Heap()
    assert heap.is_empty()
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
