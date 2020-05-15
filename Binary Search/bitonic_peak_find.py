"""Finding a bitonic peak in an array
Bitonically sorted array is a sequence that
starts off with the increasing terms and then
concludes with the decreasing terms. The largest
term in this sequence is called the Bitonic Peak"""


def find_highest_number(an_array):
    low = 0
    high = len(an_array) - 1

    # Require at least 3 elements for a bitonic sequence
    if len(an_array) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        mid_left = an_array[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = an_array[mid + 1] if mid + 1 < len(an_array) else float("inf")

        if mid_left < an_array[mid] < mid_right:
            low = mid + 1
        elif mid_left > an_array[mid] > mid_right:
            high = mid - 1
        elif mid_left < an_array[mid] > mid_right:
            return an_array[mid]

    return None


# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))
