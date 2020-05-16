"""Finding the smallest number in a cyclically shifted array"""


def find(an_array):
    low = 0
    high = len(an_array) - 1

    while low < high:
        mid = (low + high) // 2

        if an_array[mid] <= an_array[high]:
            high = mid
        elif an_array[mid] > an_array[high]:
            low = mid + 1

    return low


A = [4, 5, 6, 7, 1, 2, 3]
INDEX = find(A)
print(A[INDEX])
