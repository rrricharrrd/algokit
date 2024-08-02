from ._exception import DataStructureException


class TreeError(DataStructureException):
    pass


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        pass

    def find(self, data):
        pass

    def is_empty(self):
        return self.root is None

    def __str__(self):
        return "Tree<TODO>"
