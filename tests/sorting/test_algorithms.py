import random

from interviews.sorting.algorithms import heapsort

RNG = random.Random(123)


def test_heapsort_empty():
    items = []
    result = heapsort(items)
    assert result == sorted(items)


def test_heapsort_sorted():
    items = list(range(100))
    result = heapsort(items)
    assert result == sorted(items)


def test_heapsort():
    items = list(range(100))
    for _ in range(5):
        RNG.shuffle(items)
        result = heapsort(items)
        assert result == sorted(items)
