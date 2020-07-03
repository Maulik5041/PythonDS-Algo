"""Binary search to find the index of the given key in a sorted array"""


# Iterative approach: Better Space complexity
def find_idx(an_array, the_key):

    # Using *not an_array* would consider a value 0
    # as None. But 0 is also a valid value. Thus, to
    # avoid that, explicitly mention
    # an_array or the_key is None
    if an_array is None or the_key is None:
        return -1

    length = len(an_array) - 1
    left = 0
    right = length

    while left <= right:

        mid = left + ((right - left)//2)

        if an_array[mid] == the_key:
            return mid

        if an_array[mid] < the_key:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Recursive approach: Memory of O(log n) due to recursive stack
def find_idx_rec(an_array, the_key):
    if an_array is None or the_key is None:
        return -1

    left = 0
    right = len(an_array) - 1

    return helper(an_array, the_key, left, right)


def helper(an_array, the_key, left, right):

    if left > right:
        return -1

    mid = left + ((right - left)//2)

    if the_key == an_array[mid]:
        return mid

    if the_key < an_array[mid]:
        return helper(an_array, the_key, left, mid-1)

    if the_key > an_array[mid]:
        return helper(an_array, the_key, mid+1, right)


def find_idx_test():

    assert find_idx(None, 45) == -1
    assert find_idx([2, 5, 6, 7], None) == -1
    assert find_idx([-1, 0, 7, 8, 9], 8) == 3
    assert find_idx([1], 2) == -1
    assert find_idx([0, 1, 2], 0) == 0
    assert find_idx([34, 89, 123, 890, 4567, 343568], 4567) == 4
    print("All test cases passed iteratively")

    assert find_idx_rec(None, 45) == -1
    assert find_idx_rec([2, 5, 6, 7], None) == -1
    assert find_idx_rec([-1, 0, 7, 8, 9], 8) == 3
    assert find_idx_rec([1], 2) == -1
    assert find_idx_rec([0, 1, 2], 0) == 0
    assert find_idx_rec([34, 89, 123, 890, 4567, 343568], 4567) == 4
    print("All test cases passed recursively")


if __name__ == '__main__':
    find_idx_test()
