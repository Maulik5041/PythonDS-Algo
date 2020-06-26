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


def bfs(my_graph, source):
    visited = [False] * len(my_graph.graph)

    queue = []
    result = ""

    queue.append(source)
    visited[source] = True

    while queue:
        source = queue.pop(0)
        result += str(source)

        while my_graph.graph[source]:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
            my_graph.graph[source] = my_graph.graph[source].next

    return result


if __name__ == '__main__':
    
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(bfs(g, 0))
