from data_structures import Heap


def test_heap():
    h = Heap()

    h.insert(1)
    h.print()

    h.insert(3)
    h.print()

    h.insert(2)
    h.print()
