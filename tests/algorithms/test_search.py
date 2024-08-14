from algokit.algorithms.search import bfs, dfs
from algokit.data_structures import Graph


def _make_graph():
    r"""
    [0] -> [1] <- [2]
     |  \   |  \   ^
     V   >  V    > |
    [5]    [4] <- [3]
    """
    graph = Graph()
    n0 = graph.add_node(0)
    n1 = graph.add_node(1)
    n2 = graph.add_node(2)
    n3 = graph.add_node(3)
    n4 = graph.add_node(4)
    n5 = graph.add_node(5)
    nodes = [n0, n1, n2, n3, n4, n5]  # in case internal representation changes order
    graph.add_directed_edge(nodes[0], nodes[1])
    graph.add_directed_edge(nodes[0], nodes[4])
    graph.add_directed_edge(nodes[0], nodes[5])
    graph.add_directed_edge(nodes[1], nodes[3])
    graph.add_directed_edge(nodes[1], nodes[4])
    graph.add_directed_edge(nodes[2], nodes[1])
    graph.add_directed_edge(nodes[3], nodes[2])
    graph.add_directed_edge(nodes[3], nodes[4])
    return graph, nodes


def test_bfs():
    _, nodes = _make_graph()

    result = bfs(nodes[0], 2)
    assert result == nodes[2]

    result = bfs(nodes[1], 5)
    assert result is None

    result = bfs(nodes[1], 1)
    assert result == nodes[1]


def test_dfs():
    _, nodes = _make_graph()

    result = dfs(nodes[0], 2)
    assert result == nodes[2]

    result = dfs(nodes[1], 5)
    assert result is None

    result = dfs(nodes[1], 1)
    assert result == nodes[1]
