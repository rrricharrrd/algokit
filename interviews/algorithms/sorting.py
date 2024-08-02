from interviews.data_structures import Heap


def heapsort(items):
    if len(items) == 0:
        return items

    result = []
    heap = Heap.heapify(items)
    while not heap.is_empty():
        minimum = heap.extract_min()
        result.append(minimum)
    return result
