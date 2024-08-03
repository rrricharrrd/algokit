from ._exception import DataStructureException

END = "*"


class TrieError(DataStructureException):
    pass


class TrieNode:
    def __init__(self, data=None):
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode(data=None)

    def is_empty(self):
        return not bool(self.root.children)

    def insert(self, items):
        here = self.root
        for item in items:
            child = here.children.get(item)
            if child is None:
                child = TrieNode(data=item)
                here.children[item] = child
            here = child
        here.children[END] = TrieNode(data=END)

    def search(self, items):
        here = self.root
        for item in items:
            try:
                child = here.children[item]
            except KeyError:
                raise TrieError(f"Entry {items} not found; failure at {item}")
            here = child
        if END in here.children:
            return items
        else:
            raise TrieError(f"Entry {items} found but not a terminated entry")
