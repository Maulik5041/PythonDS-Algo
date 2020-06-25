def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row-1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dir_matrix = 0
    while (top <= bottom and left <= right):
        if dir_matrix == 0:
            for i in range(left,right+1): # moving left->right
                print (arr[top][i], end=" ")

            # Since we have traversed the whole first
            # row, move down to the next row.
            top +=1
            dir_matrix = 1

        elif dir_matrix == 1:
            for i in range(top, bottom+1):  # moving top->bottom
                print(arr[i][right], end=" ")

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -= 1
            dir_matrix = 2
        elif dir_matrix == 2:
            for i in range(right, left-1, -1):  # moving right->left
                print(arr[bottom][i], end=" ")

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -=1
            dir_matrix = 3

        elif dir_matrix == 3:
            for i in range(bottom, top-1, -1):  # moving bottom->top
                print(arr[i][left], end=" ")
            # Since we have traversed the whole first
            # column, move down to the next column.
            left += 1
            dir_matrix = 0


# Driver code
# Change the following array and the corresponding row and
# column arguments to test on some other input
array = [[1,2,3,4],
     [12,13,14,5],
     [11,16,15,6],
     [10,9,8,7]]

spiralMatrixPrint(4, 4, array)
