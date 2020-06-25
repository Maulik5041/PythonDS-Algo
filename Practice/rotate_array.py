"""Rotate an array by N Elements"""


def rotate_array(arr, n):
    if arr is None or len(arr) == 0:
        return None

    length = len(arr)

    # normalize the rotations if n > length
    n = n % length

    if n < 0:
        n = n + length

    # reversing the entire array
    reverse_array(arr, 0, length-1)

    # reversing the targeted elements only
    reverse_array(arr, 0, n-1)

    # reversing the remaining array
    reverse_array(arr, n, length-1)
    return arr


def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def test_rotations():
    assert rotate_array([], 5) is None
    assert rotate_array([9], 2) == [9]
    assert rotate_array([3, 6, 19, 0, 23], -3) == [0, 23, 3, 6, 19]
    assert rotate_array([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    test_rotations()
    print("Successfully passed")
