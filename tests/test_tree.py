from data_structures import Tree


def test_empty():
    tree = Tree()
    assert tree.is_empty()
    print(tree)


def test_tree():
    tree = Tree()
    tree.insert(1)
    print(tree)
