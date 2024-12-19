import hashlib
import random
from typing import Any, Callable, Optional


def _make_hash_function(salt: Any) -> Callable:
    def hash_function(x: Any) -> int:
        hasher = hashlib.sha256()
        hasher.update(str(salt).encode() + str(x).encode())
        return int(hasher.hexdigest(), 16)

    return hash_function


class BloomFilter:
    def __init__(self, n_filters: int, filter_size: int, rng: Optional[random.Random] = None):
        self._rng = rng or random.Random(123)
        self._hash_functions = [_make_hash_function(i) for i in self._rng.sample(range(0, 10 * n_filters), n_filters)]
        self._filter_size = filter_size
        self._buckets = [[0 for _ in range(filter_size)] for _ in range(n_filters)]

    def add(self, x: Any) -> None:
        for ix, hf in enumerate(self._hash_functions):
            h = hf(x) % self._filter_size
            self._buckets[ix][h] = 1

    def query(self, x: Any) -> bool:
        for ix, hf in enumerate(self._hash_functions):
            h = hf(x) % self._filter_size
            if self._buckets[ix][h] != 1:
                return False
        return True
