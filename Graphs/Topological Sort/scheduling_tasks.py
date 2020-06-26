from collections import deque


def is_scheduling(tasks, prerequisites):
    if tasks <= 0:
        return False

    sorted_order = []

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for edge in prerequisites:
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

    return len(sorted_order) == tasks


print("Is scheduling possible: " +
    str(is_scheduling(3, [[0, 1], [1, 2]])))
print("Is scheduling possible: " +
    str(is_scheduling(3, [[0, 1], [1, 2], [2, 0]])))
print("Is scheduling possible: " +
    str(is_scheduling(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))
