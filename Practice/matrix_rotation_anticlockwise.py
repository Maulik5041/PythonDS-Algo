"""Rotate an image/matrix in reverse"""


def rotate_matrix(matrix):
    N = len(matrix)

    # Consider all squares one by one
    for i in range(0, N):
        print(i)

        # Consider elements in group of 4
        for j in range(i, N-i-1):
            print(i, j)

            # store current cell in temp variable
            temp = matrix[i][j]

            # Only rotating 4 points of a square one at a time
            matrix[i][j] = matrix[j][N-1-i]
            matrix[j][N-1-i] = matrix[N-1-i][N-1-j]
            matrix[N-1-i][N-1-j] = matrix[N-1-j][i]
            matrix[N-1-j][i] = temp


def displayMatrix(matrix):
    N = len(matrix)
    for i in range(0, N):
        for j in range(0, N):
            print(matrix[i][j], end=' ')
        print("")


matrix_1 = [[1, 2, 3, 4, 4],
        [5, 6, 7, 8, 8],
        [9, 10, 11, 12, 12],
        [13, 14, 15, 16, 16],
        [17, 18, 19, 20, 20]]

rotate_matrix(matrix_1)
displayMatrix(matrix_1)
