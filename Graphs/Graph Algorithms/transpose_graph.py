class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def print_graph(self):
        for a_vertex in range(self.V):
            temp = self.graph[a_vertex]
            while temp:
                print(temp.vertex)
                temp = temp.next


def transpose(my_graph):
    new_graph = Graph(my_graph.V)

    for source in range(my_graph.V):
        while my_graph.graph[source]:
            destination = my_graph.graph[source].vertex
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph


V = 5
g = Graph(V)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

new_g = transpose(g)
new_g.print_graph()
