from heapq import heappop, heappush


def sort_char(str):
    freq_char_map = {}
    for char in str:
        freq_char_map[char] = freq_char_map.get(char, 0) + 1

    max_heap = []
    for char, freq in freq_char_map.items():
        heappush(max_heap, (-freq, char))

    sorted_str = []
    while max_heap:
        freq, char = heappop(max_heap)
        for _ in range(-freq):
            sorted_str.append(char)

    return ''.join(sorted_str)


print("String after sorting characters by frequency: " +
sort_char("Programming"))
print("String after sorting characters by frequency: " +
sort_char("abcbab"))
