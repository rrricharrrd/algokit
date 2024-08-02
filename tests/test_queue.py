from data_structures import Queue


def test_empty():
    queue = Queue()
    print(queue)


def test_queue():

    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.remove()
    print(queue)
