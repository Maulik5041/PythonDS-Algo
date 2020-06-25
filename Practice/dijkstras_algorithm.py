"""Implementing Dijkstra's algorithm to find the shortest path"""


def to_be_visited(v_d):
    v = -10
    for idx in range(tot_vertices):
        if v_d[idx][0] == 0 and (v < 0 or v_d[idx][1] <= v_d[v][1]):
            v = idx
    return v


# Creating the graph as an adjacency matrix
vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
edges = [[0, 3, 4, 0],
          [0, 0, 0.5, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]


tot_vertices = len(vertices[0])

visited_dist = [[0, 0]]

for i in range(tot_vertices-1):
    visited_dist.append([0, float("inf")])

for vertex in range(tot_vertices):
    to_visit = to_be_visited(visited_dist)

    for neighbor_index in range(tot_vertices):

        if vertices[to_visit][neighbor_index] == 1 and visited_dist[neighbor_index][0] == 0:
            new_distance = visited_dist[to_visit][1] + edges[to_visit][neighbor_index]

            if visited_dist[neighbor_index][1] > new_distance:
                visited_dist[neighbor_index][1] = new_distance

        visited_dist[to_visit][0] = 1

i = 0

for distance in visited_dist:
    print(f"The shortest distance of {(chr(ord('a') + i))} from the source vertex a is:{distance[1]}")
    i = i + 1
