def generateMatrix(n):

    A = [[0] * n for _ in range(n)]

    i = 0 
    j = 0
    di = 0
    dj = 1

    for k in range(n*n):
        print(f"Different values of k: {k}")
        print(f"A[i][j] = {A[i][j]}")
        A[i][j] = k + 1
        print(f"A[(i+di) % n][(j+dj) % n] = {(i + di) % n} and {(j + dj) % n}")
        print(f"Shorter values of d's : {di} {dj}")
        if A[(i+di) % n][(j+dj) % n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


print(generateMatrix(3))


def generateMatrix2(n):

    if not n:
        return []

    res = [[0 for _ in range(n)] for _ in range(n)]

    left, right, top, bottom, num = 0, n-1, 0, n-1, 1

    while left <= right and top <= bottom:

        for i in range(left, right+1):
            res[top][i] = num
            num += 1

        top += 1

        for i in range(top, bottom+1):
            res[i][right] = num
            num += 1

        right -= 1

        for i in range(right, left-1, -1):
            res[bottom][i] = num
            num += 1

        bottom -= 1

        for i in range(bottom, top-1, -1):
            res[i][left] = num
            num += 1

        left += 1

    return res


print(generateMatrix2(7))
