"""Find the largest continuous sum from an array"""


def large_cont_sum(an_array):

    if not an_array:
        return

    if len(an_array) == 0:
        return 0

    max_sum = curr_max = an_array[0]
    max_values = []

    left_idx, right_idx = an_array[0], an_array[1]

    for a_value in an_array[1:]:

        curr_max = max(curr_max+a_value, a_value)
        max_sum = max(curr_max, max_sum)

    return max_sum


def large_cont_sum_test():

    assert large_cont_sum([]) is None
    assert large_cont_sum(None) is None
    assert large_cont_sum([7, 1, -3, 0, 2, -3, -5, 11]) == 11
    assert large_cont_sum([1, 2, 3, 4, 5, 6, 7, 8]) == 36


if __name__ == '__main__':
    large_cont_sum_test()
    print('All test cases passed')
