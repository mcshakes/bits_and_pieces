from vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_of_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contain__(self, n):
        return n in self.vert_list

    def add_edge(self, source, dest, weight=0):
        if source not in self.vert_list:
            new_vert = self.add_vertex(source)

        if dest not in self.vert_list:
            new_vert = self.add_vertex(dest)

        self.vert_list[source].add_neighbor(self.vert_list[dest], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())
