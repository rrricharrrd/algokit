import pytest

from data_structures import Tree, TreeError


def test_empty():
    tree = Tree()
    assert tree.is_empty()
    assert len(tree) == 0
    print(tree)


def test_errors():
    tree = Tree()
    with pytest.raises(TreeError):
        tree.peek()


def test_tree():
    tree = Tree()
    tree.insert(1)
    print(tree)
