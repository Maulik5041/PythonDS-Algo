def surround_regions(board):
    q = []

    r, c = len(board), len(board[0])
    if r == 0 or c == 0:
        return

    for i in range(r):
        for j in range(c):
            if (i == 0 or j == 0 or i == r - 1 or j == c - 1) and board[i][j] == 'o':
                q.append((i, j))

    while q:
        i, j = q.pop(0)
        board[i][j] = 'T'
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x_n = i + x
            y_n = j + y

            if x_n >= 0 and x_n < r and y_n >= 0 and y_n < c and board[x_n][y_n] == 'o':
                q.append((x_n, y_n))

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'o':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'o'

