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
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}\n head", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print("\n")


def dfs(my_graph, source):
    visited = [False] * len(my_graph.graph)

    stack = []

    result = ""

    stack.append(source)
    visited[source] = True

    while stack:
        source = stack.pop()
        result += str(source)

        while my_graph.graph[source]:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            my_graph.graph[source] = my_graph.graph[source].next
    return result


V = 5
g = Graph(V)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

print(dfs(g, 0))
g.print_graph()
