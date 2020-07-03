"""Find the low and high index of a key in sorted array"""


def find_low_index(array, key):

    if not array or not key:
        return -1

    left = 0
    right = len(array) - 1
    mid = right // 2

    while left <= right:

        mid_elem = array[mid]

        if mid_elem < key:
            left = mid + 1
        else:
            right = mid - 1

        mid = left + ((right - left) // 2)

    if left < len(array) and array[left] == key:
        return left

    return -1


def find_high_index(array, key):

    if not array or not key:
        return -1

    left = 0
    right = len(array) - 1
    mid = right // 2

    while left <= right:

        mid_elem = array[mid]

        if mid_elem > key:
            right = mid - 1
        else:
            left = mid + 1

        mid = left + ((right - left) // 2)

    if right < len(array) and array[right] == key:
        return right

    return -1


def find_indexes_test():

    assert find_low_index([1, 1, 1, 1, 2, 3, 3, 4, 4, 5], 1) == 0
    assert find_low_index([], 1) == -1
    assert find_low_index([1, 2, 3, 4], None) == -1
    assert find_low_index([1, 2, 3], 3) == 2
    print("All test cases passed for low index")

    assert find_high_index([1, 1, 1, 1, 2, 3, 3, 4, 4, 5], 1) == 3
    assert find_high_index([], 1) == -1
    assert find_high_index([1, 2, 3, 4], None) == -1
    assert find_high_index([1, 2, 3, 3, 4, 5], 3) == 3
    print("All tests cases passed for high index")


if __name__ == '__main__':
    find_indexes_test()
