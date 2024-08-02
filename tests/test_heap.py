from data_structures import Heap


def test_empty():
    heap = Heap()
    print(heap)


def test_heap():
    heap = Heap()
    heap.insert(1)
    heap.insert(3)
    heap.insert(2)
    print(heap)
