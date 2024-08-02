from interviews.data_structures import Graph


def test_empty():
    graph = Graph()
    assert graph.is_empty()
    assert len(graph) == 0
    print(graph)


def test_graph():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    _ = graph.add_node(3)
    graph.add_edge(node1, node2)

    print(graph)
    assert len(graph) == 3
