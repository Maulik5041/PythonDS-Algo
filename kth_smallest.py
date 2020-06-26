"""Very popular problem. Could be solved with multiple algorithms"""


from heapq import heappush, heappop


# Method 1: Brute-force
def k_small_brute(nums, k):
    prev_small, prev_small_idx = float('-inf'), -1
    curr_small, curr_small_idx = float('idx'), -1

    for i in range(k):
        for j in range(len(nums)):
            if nums[j] > prev_small and nums[j] < curr_small:
                curr_small = nums[j]
                curr_small_idx = j

            elif nums[j] == prev_small and j > prev_small_idx:
                curr_small = nums[j]
                curr_small_idx = j
                break

        prev_small = curr_small
        prev_small_idx = curr_small_idx
        curr_small = float('inf')

    return prev_small


# Method 2: Max Heap
def k_small_max_heap(nums2, k2):
    max_heap = []

    for i in range(k2):
        heappush(max_heap, -nums2[i])

    for i in range(k2, len(nums2)):
        if -nums2[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums2[i])

    return -max_heap[0]


# Method 3: Min Heap
# Complexity of Max is better than Min

# Method 4: Median of Medians Quick Sort --> Best Complexity [O(N)]
