"""Rotation of matrix/image clockwise"""


# Successful rotation could be achieved by transposing
# and then reversing the columns
def rotate90(arr):
    col_size = len(arr[0])
    row_size = len(arr)
    transpose(arr, row_size, col_size)
    reverse_col(arr, row_size, col_size)


def transpose(arr, row_size, col_size):
    for i in range(row_size):
        for j in range(i, col_size):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


def reverse_col(arr, row_size, col_size):
    for i in range(col_size):
        j = 0
        k = col_size - 1
        while j < k:
            arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
            j += 1
            k -= 1


# Function for print matrix
def printMatrix(arr):
    row_size = len(arr)
    col_size = len(arr[0])
    for i in range(row_size):
        for j in range(col_size):
            print(str(arr[i][j]), end=" ")
        print()


arr_1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]

print("\n----Before Rotation----\n")
printMatrix(arr_1)

rotate90(arr_1)

print("----After Rotation----\n")
printMatrix(arr_1)
