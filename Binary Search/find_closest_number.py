"""Finding the closest number by using Binary Search"""


def find_closest_num(an_array, target):
    min_diff = float("inf")
    low = 0
    high = len(an_array) - 1
    closest_num = None

    # Edge cases:
    # Empty list and Single Element
    if len(an_array) == 0:
        return None
    if len(an_array) == 1:
        return an_array[0]

    while low <= high:
        mid = (low + high) // 2

        # Keeping the search in bounds
        if mid + 1 < len(an_array):
            min_diff_right = abs(an_array[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(an_array[mid - 1] - target)

        # Check if the absolute value between left and right
        # elements are smaller than seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = an_array[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = an_array[mid + 1]

        # Move the mid-point appropriately as is done
        # via Binary Search
        if an_array[mid] < target:
            low = mid + 1
        elif an_array[mid] > target:
            high = mid - 1
        else:
            return an_array[mid]

    return closest_num


A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

print(find_closest_num(A1, 11))
print(find_closest_num(A2, 4))
