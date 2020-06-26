from heapq import heappop, heappush


def find_kth_smallest(matrix, k):
    min_heap = []

    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    number_count, number = 0, 0
    while min_heap:
        number, i, row = heappop(min_heap)
        number_count += 1
        if number_count == k:
            break

        if len(row) > i+1:
            heappush(min_heap, (row[i+1], i+1, row))

    return number


print("Kth smallest number is: " +
  str(find_kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))
