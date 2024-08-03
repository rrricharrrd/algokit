import pytest

from interviews.data_structures import Trie, TrieError


def test_empty():
    trie = Trie()
    assert trie.is_empty()


def test_search():
    trie = Trie()
    trie.insert("ABC")
    trie.insert("ABCD")
    trie.insert("ABCEF")
    trie.insert("ABCEG")
    trie.insert("ABCEGH")
    trie.insert("XYZ")
    assert len(trie.root.children) == 2

    trie.search("ABC")
    trie.search("ABCEGH")
    with pytest.raises(TrieError):
        trie.search("123")
    with pytest.raises(TrieError):
        trie.search("ABCE")
