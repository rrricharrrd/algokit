from algokit.data_structures.probabilistic import BloomFilter


def test_true_positive():
    bf = BloomFilter(n_filters=3, filter_size=16)

    bf.add(0)
    bf.add(10)

    assert bf.query(0)
    assert bf.query(10)


def test_false_positive():
    bf = BloomFilter(n_filters=3, filter_size=4)

    bf.add(0)
    bf.add(1)

    count = 0
    for i in range(2, 1000):
        count += int(bf.query(i))
    assert count > 0  # TODO improve check with better bounds
