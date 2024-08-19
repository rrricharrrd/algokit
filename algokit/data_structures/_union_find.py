from ._exception import DataStructureException


class UnionFindError(DataStructureException):
    pass


class UnionFind:
    """TODO: path compression"""

    def __init__(self, size):
        self.parents = list(range(size))

    def __str__(self):
        return f"UnionFind<{self.parents}>"

    def __len__(self):
        return len(self.parents)

    def is_empty(self):
        return len(self) == 0

    def find(self, x):
        if x > len(self):
            raise UnionFindError(f"Index {x} greater than size {len(self)}")

        ix = x
        while self.parents[ix] != ix:
            ix = self.parents[ix]
        return ix

    def merge(self, x, y):
        if x > len(self):
            raise UnionFindError(f"First index {x} greater than size {len(self)}")
        if y > len(self):
            raise UnionFindError(f"Second index {y} greater than size {len(self)}")

        x_root = self.find(x)
        y_root = self.find(y)
        self.parents[y_root] = x_root
