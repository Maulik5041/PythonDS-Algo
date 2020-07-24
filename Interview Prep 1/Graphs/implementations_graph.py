"""Different variations of implementing graph classes in Python"""


# Method 1: Using dictionaries to hold edges
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return f'{str(self.id)} connected to: {str([x.id for x in self.connected_to])}'

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, source, dest, cost=0):
        if source not in self.vert_list:
            self.add_vertex(source)
        if dest not in self.vert_list:
            self.add_vertex(dest)
        self.vert_list[source].add_neighbor(self.vert_list[dest], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


g = Graph()
for i in range(10):
    g.add_vertex(i)

print(f"\nThe list of vertices are:\n{g.vert_list}")

g.add_edge(0, 1, 2)
g.add_edge(1, 4, 2)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 2)
g.add_edge(4, 5, 2)
g.add_edge(6, 8, 2)
g.add_edge(7, 9, 2)

for vertex in g:
    print(f"Vertex = {vertex}")
    print(f"The connections are: {vertex.get_connections()}\n")
