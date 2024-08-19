from algokit.algorithms.sort import heap_sort
from algokit.data_structures import UnionFind


def kruskal(graph):
    edges = {}
    edges_by_weight = []
    nodes = {n: ix for ix, n in enumerate(graph.iternodes())}
    for ix, (n1, n2, weight) in enumerate(graph.iteredges()):
        edges[ix] = (n1, n2)
        edges_by_weight.append((weight, ix))
    edges_by_weight = heap_sort(edges_by_weight)

    span = []
    uf = UnionFind(size=len(graph))
    for _, ix in edges_by_weight:
        n1, n2 = edges[ix]
        u = nodes[n1]
        v = nodes[n2]
        if uf.find(u) != uf.find(v):
            span.append((n1, n2))
            uf.merge(u, v)
    return span
