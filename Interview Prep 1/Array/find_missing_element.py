"""Find the missing element from the second array"""


def finder(arr1, arr2):
    """This is an O(N) solution but could
    be problematic for very high values or
    very low values with a lot of decimals"""

    if not arr1 or not arr2:
        return None

    if len(arr1) - len(arr2) != 1:
        return None

    if len(arr1) == len(arr2):
        return None

    missing_val = arr1[len(arr1)-1]

    for idx, val in enumerate(arr2):
        missing_val += (arr1[idx] - arr2[idx])

    return missing_val


def finder2(arr1, arr2):
    """This is a better approach and has constant
    space complexity. Using XOR method"""

    if not arr1 or not arr2:
        return None

    if len(arr1) - len(arr2) != 1:
        return None

    if len(arr1) == len(arr2):
        return None

    result = 0

    for a_num in arr1+arr2:
        result ^= a_num

    return result


def finder_test():
    assert finder2(None, [1]) is None
    assert finder2(None, None) is None
    assert finder2([1, 2, 3], [1, 2, 3]) is None
    assert finder2([1, 2, 3, 4, 5, 6], [4, 5, 1, 3, 6]) == 2
    assert finder2([5, 5, 7, 7], [7, 5, 5]) == 7
    assert finder2([1, 4, 5, 6], [1, 4]) is None


if __name__ == '__main__':
    finder_test()
    print('All test cases passed')
