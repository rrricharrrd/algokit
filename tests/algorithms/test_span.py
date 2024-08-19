from algokit.algorithms.span import kruskal
from algokit.data_structures import Graph


def _make_graph():
    r"""
    [0] -- [1]    [2]
     |  \   |      |
     |   \  |      |
    [5]    [4]    [3]
    """
    graph = Graph()
    n0 = graph.add_node(0)
    n1 = graph.add_node(1)
    n2 = graph.add_node(2)
    n3 = graph.add_node(3)
    n4 = graph.add_node(4)
    n5 = graph.add_node(5)
    nodes = [n0, n1, n2, n3, n4, n5]  # in case internal representation changes order
    graph.add_edge(nodes[0], nodes[1])
    graph.add_edge(nodes[0], nodes[4])
    graph.add_edge(nodes[0], nodes[5])
    graph.add_edge(nodes[1], nodes[3])
    graph.add_edge(nodes[1], nodes[4])
    graph.add_edge(nodes[3], nodes[4])
    return graph, nodes


def test_kruskal():
    graph, nodes = _make_graph()

    span = kruskal(graph)

    assert len(span) == 4
    n0, n1, n2, n3, n4, n5 = nodes
    for edge in span:
        if n2 in edge:
            assert n3 in edge
        if n5 in edge:
            assert n0 in edge
        if n0 in edge:
            assert any([n in edge for n in {n1, n4, n5}])
