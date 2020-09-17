class Graph:
    def __init__(self):
        self.edges = {}

    def add_node(self, node):
        if node in self.edges:
            raise ValueError("is a duplicate node")
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def has_node(self, node):
        return node in self.edges

    def get_node(self, name):
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ""
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.get_name() + " ---> " + dest.get_name()
        return result
