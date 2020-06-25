"""Search in a sorted matrix"""


def search_in_matrix(matrix, key):
    if matrix is None or len(matrix) == 0:
        return (-1, -1)

    # length of rows
    M = len(matrix)

    # length of columns
    N = len(matrix[0])

    i = 0
    j = N - 1

    while i < M and j >= 0:

        if matrix[i][j] is key:
            return (i, j)

        elif key < matrix[i][j]:
            j = j - 1

        else:
            i = i + 1

    return (-1, -1)


def test_matrix():
    assert search_in_matrix([], 90) == (-1, -1)
    assert search_in_matrix(None, 8) == (-1, -1)
    assert search_in_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 12) == (-1, -1)
    assert search_in_matrix([[2, 4, 9, 13, 15], [3, 5, 11, 18, 22], [6, 8, 16, 21, 28], [9, 11, 20, 25, 31]], 21) == (2, 3)


if __name__ == '__main__':
    test_matrix()
    print("Successful tests")
