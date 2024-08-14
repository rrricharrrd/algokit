from ._exception import DataStructureException


class GraphError(DataStructureException):
    pass


class GraphNode:
    def __init__(self, data=None):
        self.data = data
        self.adjacency = {}

    def __str__(self):
        return f"GraphNode<{self.data}>: [{','.join(str(n.data) for n in self.adjacency)}]"


class Graph:
    def __init__(self):
        self.nodes = set()

    def __str__(self):
        s = ""
        for n in self.nodes:
            if s:
                s += "; "
            s += str(n)
        return f"Graph<{s}>"

    def __len__(self):
        return len(self.nodes)

    def is_empty(self):
        return len(self) == 0

    def add_node(self, data):
        node = GraphNode(data)
        self.nodes.add(node)
        return node

    def add_directed_edge(self, node1, node2, weight=1):
        if node1 not in self.nodes:
            self.nodes.add(node1)
        if node2 not in self.nodes:
            self.nodes.add(node2)

        node1.adjacency[node2] = weight

    def add_edge(self, node1, node2, weight=1):
        self.add_directed_edge(node1, node2, weight=weight)
        self.add_directed_edge(node2, node1, weight=weight)
