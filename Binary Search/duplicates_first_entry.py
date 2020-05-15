"""Finding the first entry in list with Duplicates"""


def find(an_array, target):
    low = 0
    high = len(an_array) - 1

    while low <= high:
        mid = (low + high) // 2

        if an_array[mid] < target:
            low = mid + 1
        elif an_array[mid] > target:
            high = mid - 1

        # Getting the FIRST occurence and not just any occurence
        else:
            if mid - 1 < 0:
                return mid
            if an_array[mid - 1] != target:
                return mid
            high = mid - 1


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
TARGET = 108
x = find(A, TARGET)
print(x)
