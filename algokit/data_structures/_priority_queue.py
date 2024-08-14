import functools

from algokit.data_structures._heap import Heap


@functools.total_ordering
class PriorityQueueEntry:
    def __init__(self, data=None, priority=1):
        self.data = data
        self.priority = priority

    def __eq__(self, other):
        if not isinstance(other, PriorityQueueEntry):
            raise ValueError(f"Cannot compare to {other} of type {type(other)}")
        return self.priority == other.priority and self.data == other.data

    def __lt__(self, other):
        if not isinstance(other, PriorityQueueEntry):
            raise ValueError(f"Cannot compare to {other} of type {type(other)}")
        if self.priority == other.priority:
            return self.data < other.data  # doesn't really matter
        else:
            return self.priority < other.priority

    def __hash__(self):
        return hash((self.priority, self.data))


class PriorityQueue:
    """*Min*-priority queue."""

    def __init__(self):
        self.heap = Heap()

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        head = self.heap.peek()
        return head

    def enqueue(self, data, priority=1):
        entry = PriorityQueueEntry(data=data, priority=priority)
        self.heap.insert(entry)
        return entry

    def dequeue(self):
        minimum = self.heap.extract_min()
        return minimum

    def change_priority(self, entry, priority=1):
        index = self.heap.items.index(entry)
        old_priority = entry.priority
        entry.priority = priority
        if priority < old_priority:
            self.heap._sift_up(index)
        else:
            self.heap._sift_down(index)
