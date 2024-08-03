from interviews.data_structures import Graph, GraphNode


def test_empty():
    graph = Graph()
    assert graph.is_empty()
    assert len(graph) == 0


def test_node():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    assert node1.data == 1
    assert node2.data == 2
    assert len(graph) == 2


def test_edge():
    graph = Graph()
    node1 = graph.add_node(1)
    node2 = graph.add_node(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    assert len(graph) == 2

    graph.add_directed_edge(node1, node2)
    assert node2 in node1.adjacency
    assert node1 not in node2.adjacency
    graph.add_directed_edge(node4, node1)
    assert node1 in node4.adjacency
    assert node4 not in node1.adjacency
    assert len(graph) == 3

    graph.add_edge(node1, node3)
    assert node3 in node1.adjacency
    assert node1 in node3.adjacency
    assert len(graph) == 4


def test_str():
    graph = Graph()
    print(graph)
    node1 = graph.add_node(1)
    print(graph)
    print(node1)
    node2 = graph.add_node(2)
    print(node2)
    print(graph)
