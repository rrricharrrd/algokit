from ._exception import DataStructureException


def _parent(ix):
    return ix // 2


def _left(ix):
    return 2 * ix


def _right(ix):
    return 2 * ix + 1


class HeapError(DataStructureException):
    pass


class Heap:
    def __init__(self):
        self.items = []

    @classmethod
    def heapify(cls, items):
        heap = cls()
        for item in items:
            heap.insert(item)
        return heap

    def __str__(self):
        return f"Heap<{self.items}>"

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return not bool(self.items)

    def peek(self):
        if self.is_empty():
            raise HeapError("Empty heap")

        return self.items[0]

    def extract_min(self):
        if self.is_empty():
            raise HeapError("Empty heap")

        result = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop(-1)
        current_ix = 0
        while current_ix < len(self):
            current = self.items[current_ix]
            left_ix = _left(current_ix)
            right_ix = _right(current_ix)
            min_child_ix = None
            min_child = None
            if left_ix < len(self.items):
                left = self.items[left_ix]
                min_child_ix = left_ix
                min_child = left
            if right_ix < len(self.items):
                right = self.items[right_ix]
                if right < left:
                    min_child_ix = right_ix
                    min_child = right

            if min_child_ix is None:
                break  # Have reached bottom
            elif min_child < current:
                self.items[min_child_ix] = current
                self.items[current_ix] = min_child
                current_ix = min_child_ix
            else:
                break  # Less than both children

        return result

    def insert(self, data):
        self.items.append(data)
        current_ix = len(self.items) - 1
        parent_ix = _parent(current_ix)
        done = False
        while current_ix != 0 and not done:
            if self.items[parent_ix] > self.items[current_ix]:
                self.items[parent_ix], self.items[current_ix] = self.items[current_ix], self.items[parent_ix]
            else:
                done = True
            current_ix = parent_ix
            parent_ix = _parent(parent_ix)

    def check(self):  # For testing...
        for ix in range(len(self.items)):
            left_ix = _left(ix)
            right_ix = _right(ix)
            if left_ix < len(self.items):
                assert self.items[ix] <= self.items[left_ix]
            if right_ix < len(self.items):
                assert self.items[ix] <= self.items[right_ix]
