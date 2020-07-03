"""Find the given key in a rotated sorted array"""


# Recursive Approach: Memory complexity of O(log N) due to recursive stack
def find_key_recur(an_array, the_key):

    if an_array is None or the_key is None:
        return -1

    return key_helper(an_array, the_key, 0, len(an_array) - 1)


def key_helper(an_array, the_key, left, right):

    if left > right:
        return -1

    mid = left + ((right - left) // 2)

    if an_array[mid] == the_key:
        return mid

    if an_array[left] <= an_array[mid] and the_key >= an_array[left] and the_key <= an_array[mid]:
        return key_helper(an_array, the_key, left, mid-1)

    if an_array[mid] <= an_array[right] and the_key >= an_array[mid] and the_key <= an_array[right]:
        return key_helper(an_array, the_key, mid+1, right)

    if an_array[mid] >= an_array[right]:
        return key_helper(an_array, the_key, mid+1, right)

    if an_array[left] >= an_array[mid]:
        return key_helper(an_array, the_key, left, mid-1)

    return -1


# Iterative approach: Memory Complexity is constant
def find_key_iter(an_array, the_key):

    if an_array is None or the_key is None:
        return -1

    left = 0
    right = len(an_array) - 1

    if left > right:
        return -1

    while left <= right:

        mid = left + ((right - left) // 2)

        if an_array[mid] == the_key:
            return mid

        if an_array[left] <= an_array[mid] and the_key >= an_array[left] and the_key <= an_array[mid]:
            right = mid - 1

        elif an_array[mid] <= an_array[right] and the_key >= an_array[mid] and the_key <= an_array[right]:
            left = mid + 1

        elif an_array[left] <= an_array[mid] and an_array[mid] <= an_array[right] and the_key > an_array[right]:
            left = mid + 1

        elif an_array[left] >= an_array[mid]:
            right = mid - 1

        elif an_array[mid] >= an_array[right]:
            left = mid + 1

        else:
            return -1

    return -1


def find_key_test():

    assert find_key_recur([2, 3, 4, 5, 1], None) == -1
    assert find_key_recur(None, 6) == -1
    assert find_key_recur([2, 34, 56, 58, 0, 0.5, 1], 0) == 4
    assert find_key_recur([56, 34, 40, 41, 50, 52], 35) == -1
    assert find_key_recur([1, 2, 3, 4, 5], 4) == 3
    assert find_key_recur([100], 100) == 0
    print("All test cases passed recursively")

    assert find_key_iter([2, 3, 4, 5, 1], None) == -1
    assert find_key_iter(None, 6) == -1
    assert find_key_iter([2, 34, 56, 58, 0, 0.5, 1], 0) == 4
    assert find_key_iter([56, 34, 40, 41, 50, 52], 35) == -1
    assert find_key_iter([1, 2, 3, 4, 5], 4) == 3
    assert find_key_iter([100], 100) == 0
    print("All test cases passed iteratively")


if __name__ == '__main__':
    find_key_test()
