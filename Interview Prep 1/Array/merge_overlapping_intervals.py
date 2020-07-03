"""Merge overlapping intervals in an array of interval pairs"""


def merge_overlap(array):

    if not array:
        return

    if len(array) == 1:
        return array[0]

    start = array[0][0]
    end = array[0][1]
    result = []

    for i in range(1, len(array)):

        if array[i][0] < start and array[i][1] > end:
            start = array[i][0]
            end = array[i][1]

        elif array[i][0] < start and start <= array[i][1] < end:
            start = array[i][0]

        elif end > array[i][0] > start and array[i][1] > end:
            end = array[i][1]

    return (start, end)


print(merge_overlap([(1, 5), (3, 7), (4, 6), (6, 8)]))
