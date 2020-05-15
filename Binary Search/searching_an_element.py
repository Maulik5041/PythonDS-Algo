"""Searching for a target element by Linear Search and Binary Search"""


# Linear Search
def linear_search(data, target):
    for an_index, _ in enumerate(data):
        if data[an_index] == target:
            return True

    return False


# Binary Search - Iterative
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True

        if target < data[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return False


# Binary Search - Recursive
def binary_search_recursive(data, target, low, high):

    if low > high:
        return False

    mid = (low + high) // 2
    if target == data[mid]:
        return True

    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid - 1)

    if target > data[mid]:
        return binary_search_recursive(data, target, mid + 1, high)


Data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
TARGET = 37

print("----------------------LINEAR SEARCH-------------------")
print(linear_search(Data, TARGET), "\n")
print("-----------------BINARY SEARCH - ITERATIVE-------------------")
print(binary_search_iterative(Data, TARGET), "\n")
print("-----------------BINARY SEARCH - RECURSIVE-------------------")
print(binary_search_recursive(Data, TARGET, 0, len(Data) - 1))
