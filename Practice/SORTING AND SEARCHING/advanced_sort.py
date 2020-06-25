"""Implementation of Merge and Quick Sort"""


import random


# Sorting 1: Merge Sort
def merge_sort(lst):

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    unordered_lst = [3, 2, 5, 1, 4]
    merge_sort(unordered_lst)
    print(f"Sorted arrays by merge sort: {unordered_lst}")


# Sorting 2: Quick Sort
def quick_sort(lst2, left, right):
    if left < right:
        pi = partition(lst2, left, right)
        quick_sort(lst2, left, pi - 1)
        quick_sort(lst2, pi + 1, right)


def partition(lst2, left, right):

    pivot_index = choose_pivot(left, right)

    lst2[right], lst2[pivot_index] = lst2[pivot_index], lst2[right]

    pivot = lst2[right]
    i = left - 1

    for j in range(left, right):
        if lst2[j] <= pivot:
            i += 1
            lst2[i], lst2[j] = lst2[j], lst2[i]

    lst2[i + 1], lst2[right] = lst2[right], lst2[i + 1]
    return i + 1


def choose_pivot(left, right):
    i1 = left + random.randint(0, right - left)
    i2 = left + random.randint(0, right - left)
    i3 = left + random.randint(0, right - left)

    return max(min(i1, i2), min(max(i1, i2), i3))


if __name__ == '__main__':

    unordered_lst2 = [5, 4, 2, 1, 3]
    quick_sort(unordered_lst2, 0, len(unordered_lst2) - 1)

    # Printing Sorted list
    print(f"Sorted list by Quick Sort: {unordered_lst2}")
