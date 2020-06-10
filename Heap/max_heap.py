"""Implementation of Max Heap"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolate_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def remove_max(self):
        if len(self.heap) > 1:
            max_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return max_val

        if len(self.heap) == 1:
            max_val = self.heap[0]
            del self.heap[0]
            return max_val

        return None

    def __percolate_up(self, index):
        parent = (index - 1)//2  # The parent of index is found by this formula
        if index <= 0:
            return

        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolate_up(parent)

    def __max_heapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__max_heapify(largest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__max_heapify(i)


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.get_max())
