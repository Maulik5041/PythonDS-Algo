from heapq import heappop, heappush


def find_k_frequent_numbers(nums, k):
    num_frequency = {}
    for num in nums:
        num_frequency[num] = num_frequency.get(num, 0) + 1

    min_heap = []

    for num, freq in num_frequency.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)

    top_numbers = []
    while min_heap:
        top_numbers.append(heappop(min_heap)[1])

    return top_numbers


print("Here are the K frequent numbers: " +
str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

print("Here are the K frequent numbers: " +
str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))
