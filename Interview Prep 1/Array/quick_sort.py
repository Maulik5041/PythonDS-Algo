"""Sort an array in ascending order by Quicksort algorithm
1. Pick a pivot number
2. Partition based on the Pivot
3. Sort it
"""


import random


def choose_pivot(left, right):
    """
    Function to choose pivot point
    :param left: Left index of sub-list
    :param right: Right index of sub-list
    """

    # Pick 3 random numbers within the range of list
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    return max(min(i1, i2), min(max(i1, i2), i3))


def partition(array, left, right):
    """
    Partition the list on the basis of pivot
    :param left: Left index of the sub-list
    :param right: Right index of the sub-list
    """

    # Index of Pivot
    pivot_index = choose_pivot(left, right)

    # Put the pivot at the end
    array[right], array[pivot_index] = array[pivot_index], array[right]

    # Selecting the pivot element
    pivot = array[right]

    # All the elements less than or equal to pivot goes
    # before or at i
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]

    return i + 1


def quick_sort_helper(array, left, right):
    """Function to sort left and right sub-array
    :param array: The given unsorted array
    :param left: Left index of the sub-list
    :param right: Right index of the sub-list
    """

    if left < right:

        # pi is where the pivot is at
        pi = partition(array, left, right)

        # Separately sort elements before and after
        # the partition index
        quick_sort_helper(array, left, pi - 1)
        quick_sort_helper(array, pi + 1, right)

    return array


def quick_sort(array):
    """Main function to sort an array
    :param array: Unsorted array
    """

    if not array:
        return None

    if len(array) == 1:
        return array

    return quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_test():

    assert quick_sort(None) is None
    assert quick_sort([1]) == [1]
    assert quick_sort([2, 5, 6, 8, 1, 3]) == [1, 2, 3, 5, 6, 8]
    assert quick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert quick_sort([-1, -3, 0, 1, -5]) == [-5, -3, -1, 0, 1]
    print("All test cases passed")


if __name__ == '__main__':
    quick_sort_test()
