import hashlib
from typing import Any, Callable

import numpy as np


def _make_hash_function(salt: Any) -> Callable:
    def hash_function(x: Any) -> int:
        hasher = hashlib.sha256()
        hasher.update(str(salt).encode() + str(x).encode())
        return int(hasher.hexdigest(), 16)

    return hash_function


class BloomFilter:
    def __init__(self, n_filters, filter_size):
        self._hash_functions = [_make_hash_function(i) for i in range(n_filters)]
        self._filter_size = filter_size
        self._buckets = np.zeros((n_filters, filter_size))

    def add(self, x: Any) -> None:
        for ix, hf in enumerate(self._hash_functions):
            h = hf(x) % self._filter_size
            self._buckets[ix, h] = 1

    def query(self, x: Any) -> bool:
        for ix, hf in enumerate(self._hash_functions):
            h = hf(x) % self._filter_size
            if self._buckets[ix, h] != 1:
                return False
        return True
