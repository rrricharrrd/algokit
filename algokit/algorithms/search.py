import logging

from algokit.data_structures import Queue

logging.getLogger().setLevel(logging.INFO)


def dfs(start, item, visited=None):
    if visited is None:
        visited = set()

    if start.data == item:
        return start

    for child in start.adjacency:
        if child not in visited:
            logging.debug(f"Visiting node {child.data}")
            visited.add(child)
            start = dfs(child, item, visited)
            try:
                visited.remove(child)
            except KeyError:
                pass
            if start is not None:
                return start
    return None


def bfs(start, item):
    queue = Queue()
    visited = set()
    queue.add(start)
    visited.add(start)

    while not queue.is_empty():
        here = queue.remove()
        logging.debug(f"Processing node {here.data}")
        if here.data == item:
            return here

        for child in here.adjacency:
            if child not in visited:
                logging.debug(f"Enqueuing node {child.data}")
                queue.add(child)
                visited.add(child)

    return None
