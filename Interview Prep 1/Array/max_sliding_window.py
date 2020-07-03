"""Find the maximum in the window size given"""


from collections import deque


def max_val(an_array, win_size):

    final_vals = []

    if not an_array or len(an_array) == 0 or win_size == 0:
        return final_vals

    if win_size > len(an_array):
        return final_vals

    window = deque()

    for i in range(0, win_size):
        while window and (an_array[i] >= an_array[window[-1]]):
            window.pop()
        window.append(i)

    final_vals.append(an_array[window[0]])

    for i in range(win_size, len(an_array)):
        while window and (an_array[i] >= an_array[window[-1]]):
            window.pop()

        if window and (window[0] <= i - win_size):
            window.popleft()

        window.append(i)
        final_vals.append(an_array[window[0]])

    return final_vals


def max_val_test():

    assert max_val(None, 2) == []
    assert max_val([], 8) == []
    assert max_val([2, 5, 3], 4) == []
    assert max_val([1, 2, 3], 3) == [3]
    assert max_val([2, 5, 6, 7, 8], 1) == [2, 5, 6, 7, 8]
    assert max_val([2, 4, 5, 89], 0) == []
    assert max_val([23, 756, 213, 7890, -1, 4, 90, -67, 34, 1235.3, 1235], 4) == [7890, 7890, 7890, 7890, 90, 90, 1235.3, 1235.3]
    print("All test cases passed")


if __name__ == '__main__':
    max_val_test()
