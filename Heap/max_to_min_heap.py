"""Converting the max heap to min heap"""


def min_heapify(heap, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    smallest = index

    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left

    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right

    if smallest != index:
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp

        min_heapify(heap, smallest)

    return heap


def convert_max(max_heap):
    # All parent nodes are from first to the middle node
    for i in range((len(max_heap))//2, -1, -1):
        max_heap = min_heapify(max_heap, i)

    return max_heap


# O(logn) to call minheapify and for n/2 times
# Thus, Time = O(n logn)
max_heap = [9, 4, 7, 1, -2, 6, 5]
print(convert_max(max_heap))
