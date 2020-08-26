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


# g = Graph()
# for i in range(6):
#     g.add_vertex(i)

# g.add_edge(0, 1, 5)
# g.add_edge(0, 5, 2)
# g.add_edge(1, 2, 4)
# g.add_edge(2, 3, 9)
# g.add_edge(3, 4, 7)
# g.add_edge(3, 5, 3)
# g.add_edge(4, 0, 1)
# g.add_edge(5, 4, 8)
# g.add_edge(5, 2, 1)

# for v in g:
#     for w in v.get_connections():
#         print("( %s , %s )" % (v.get_id(), w.get_id()))
# print(my_list)
