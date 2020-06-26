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


def number_of_nodes(my_graph, level):
    source = 0

    visited = [0] * len(my_graph.graph)

    queue = []

    result = ""

    queue.append(source)
    visited[source] = 1

    while queue:
        source = queue.pop(0)

        while my_graph.graph[source]:
            data = my_graph.graph[source].vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[source] + 1
            my_graph.graph[source] = my_graph.graph[source].next

    result = 0
    for i in range(len(my_graph.graph)):
        if visited[i] == level:
            result += 1
    return result
    