from interviews.data_structures import Heap


def bubble_sort(items):
    items = list(items)
    n = len(items)
    if n <= 1:
        return items

    for i in range(n):
        for j in range(n - i - 1):  # Bubble right
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def _find_pivot(items, lo, hi):
    pivot_is_left = True
    while lo < hi:
        if items[hi] < items[lo]:
            items[hi], items[lo] = items[lo], items[hi]
            pivot_is_left = not pivot_is_left
        lo += int(pivot_is_left)
        hi -= int(not pivot_is_left)

    return lo


def _quick_sort_inner(items, lo, hi):
    if not lo < hi:
        return

    pivot = _find_pivot(items, lo, hi)
    _quick_sort_inner(items, lo, pivot - 1)
    _quick_sort_inner(items, pivot + 1, hi)


def quick_sort(items):
    items = list(items)
    n = len(items)
    if n <= 1:
        return items

    _quick_sort_inner(items, 0, n - 1)
    return items


def _interleave(l1, l2):
    merged = []
    i = 0
    j = 0
    while i < len(l1) or j < len(l2):
        if j >= len(l2):
            merged.append(l1[i])
            i += 1
        elif i >= len(l1):
            merged.append(l2[j])
            j += 1
        elif l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    return merged


def merge_sort(items):
    items = list(items)
    n = len(items)
    if n <= 1:
        return items

    half1 = merge_sort(items[0 : n // 2])
    half2 = merge_sort(items[n // 2 : n])
    return _interleave(half1, half2)


def heap_sort(items):
    if len(items) <= 1:
        return items

    result = []
    heap = Heap.heapify(items)
    while not heap.is_empty():
        minimum = heap.extract_min()
        result.append(minimum)

    return result
