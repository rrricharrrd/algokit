from data_structures import Heap


def test_heap():
    h = Heap()
    h.insert(1)
    h.insert(3)
    h.insert(2)
    print(h)
