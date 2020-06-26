from collections import deque


def topological_sort(vertices, edges):

    # Initialize an empty array
    sorted_order = []

    # If there are no vertices
    if vertices <= 0:
        return sorted_order

    # dictionary that tracks all the incoming edges
    in_degree = {i: 0 for i in range(vertices)}

    # dictionary that tracks children of parents
    graph = {i: [] for i in range(vertices)}

    # build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    print(sorted_order)
    if len(sorted_order) != vertices:
        return []

    return sorted_order


print("Topological sort: " +
    str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
print("Topological sort: " +
    str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
print("Topological sort: " +
    str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 6]])))
