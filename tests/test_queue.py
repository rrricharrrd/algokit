from data_structures import Queue


def test_queue():

    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.remove()
    print(q)
