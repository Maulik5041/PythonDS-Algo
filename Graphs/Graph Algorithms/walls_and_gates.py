from collections import deque


def walls_and_gates(rooms):
    if not rooms:
        return []

    r, c = len(rooms), len(rooms[0])
    q = deque()

    for row in range(r):
        for col in range(c):
            if rooms[row][col] == 0:
                q.append((row, col))

    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while q:
        x, y = q.popleft()
        distance = rooms[x][y] + 1
        for dx, dy in dirs:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < r and 0 <= new_y < c and rooms[new_x][new_y] == 2147483647:
                rooms[new_x][new_y] = distance
                q.append((new_x, new_y))

    return rooms
