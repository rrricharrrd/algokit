from ._exception import DataStructureException


class GraphError(DataStructureException):
    pass


class GraphNode:
    def __init__(self, data=None):
        self.data = data
        self.adjacency = []


class Graph:
    def __init__(self):
        self.nodes = set()

    def __str__(self):
        s = ""
        for n in self.nodes:
            if s:
                s += "; "
            s += f"{n.data} -> [{','.join(str(n2.data) for n2 in n.adjacency)}]"
        return f"Graph<{s}>"

    def __len__(self):
        return len(self.nodes)

    def is_empty(self):
        return len(self) == 0

    def add_node(self, data):
        node = GraphNode(data)
        self.nodes.add(node)
        return node

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes.add(node1)
        if node2 not in self.nodes:
            self.nodes.add(node2)

        node1.adjacency.append(node2)
        node2.adjacency.append(node1)
