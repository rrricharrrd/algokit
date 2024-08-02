class Heap:
    def __init__(self):
        self.nodes = []

    def extract_min(self):
        pass  # TODO
        # min = self.nodes[0]
        # self.nodes[0] = self.nodes[-1]

    def insert(self, data):
        self.nodes.append(data)
        current = len(self.nodes) - 1
        parent = current // 2
        done = False
        while current != 0 and not done:
            if self.nodes[parent] > self.nodes[current]:
                self.nodes[parent], self.nodes[current] = self.nodes[current], self.nodes[parent]
            else:
                done = True
            current = parent
            parent = parent // 2

    def print(self):
        return self.nodes
