from algokit.data_structures.probabilistic import BloomFilter


def test_true_positive():
    bf = BloomFilter(n_filters=3, filter_size=16)

    bf.add(1)
    bf.add(2)

    assert bf.query(1)
    assert bf.query(2)


def test_false_positive():
    pass  # TODO
