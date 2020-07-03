"""Rotate an array by N elements"""


# Method 1: In-place and thus constant memory complexity
def rotate_array1(an_array, by_num):

    if not an_array:
        return None

    if by_num == 0:
        return an_array

    by_num = by_num % 10
    length = len(an_array)

    if by_num < 0:
        by_num += length

    reversed_array(an_array, 0, length - 1)
    reversed_array(an_array, 0, by_num - 1)
    reversed_array(an_array, by_num, length - 1)


def reversed_array(arr, left, right):

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1


def rotate_array_2(an_array, by_num):

    if an_array is None:
        return None

    if by_num == 0:
        return an_array

    length = len(an_array)
    temp_arr = []

    for i in range(length - by_num, length):
        temp_arr.append(an_array[i])

    for i in range(length - 1, by_num - 1, -1):
        an_array[i] = an_array[i - by_num]

    for i in range(by_num):
        an_array[i] = temp_arr[i]


def rotate_array_test():

    assert rotate_array1([], 2) is None
    assert rotate_array1([1, 2], -3) == [2, 1]
    assert rotate_array1([10, 14, 35, 67, 78, 90], 16) == [10, 14, 35, 67, 78, 90]
    assert rotate_array1([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    print("All test cases passed by Method 1")

    assert rotate_array_2([], 2) is None
    assert rotate_array_2([1, 2], -3) == [2, 1]
    assert rotate_array_2([10, 14, 35, 67, 78, 90], 16) == [10, 14, 35, 67, 78, 90]
    assert rotate_array_2([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    print("All test cases passed by Method 2")


if __name__ == '__main__':
    rotate_array_test()