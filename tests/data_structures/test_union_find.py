import pytest

from algokit.data_structures import UnionFind, UnionFindError


def test_empty():
    uf = UnionFind(size=0)
    assert uf.is_empty()
    assert len(uf) == 0


def test_errors():
    uf = UnionFind(size=5)
    with pytest.raises(UnionFindError):
        uf.find(10)
    with pytest.raises(UnionFindError):
        uf.merge(2, 10)
    with pytest.raises(UnionFindError):
        uf.merge(10, 2)


def test_merge_find():
    uf = UnionFind(size=6)
    uf.merge(0, 1)
    uf.merge(1, 2)
    uf.merge(3, 4)

    group1 = uf.find(0)
    for i in {0, 1, 2}:
        assert uf.find(i) == group1
    group2 = uf.find(3)
    for i in {3, 4}:
        assert uf.find(i) == group2
    group3 = uf.find(5)
    assert group3 == 5
    assert len({group1, group2, group3}) == 3


def test_str():
    uf = UnionFind(size=3)
    print(uf)
    uf.merge(1, 2)
    print(uf)
