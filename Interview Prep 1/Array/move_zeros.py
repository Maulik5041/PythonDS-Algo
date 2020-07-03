"""Move all the zeros to the beginning of the array"""


def move_zeros_left(an_array):

    if not an_array or len(an_array) < 1:
        return

    length = len(an_array)
    read_idx = length - 1
    write_idx = length - 1

    while read_idx >= 0:

        if an_array[read_idx] != 0:
            an_array[write_idx] = an_array[read_idx]
            write_idx -= 1

        read_idx -= 1

    while write_idx >= 0:
        an_array[write_idx] = 0
        write_idx -= 1

    return an_array


def move_zeros_test():

    assert move_zeros_left(None) is None
    assert move_zeros_left([]) is None
    assert move_zeros_left([0, 0, 1, 3, 45, 0, 0, 23, 1, 0]) == [0, 0, 0, 0, 0, 1, 3, 45, 23, 1]
    assert move_zeros_left([10, 2, 9, 0, 23, 1, -1, 0]) == [0, 0, 10, 2, 9, 23, 1, -1]
    assert move_zeros_left([7, 8, 9]) == [7, 8, 9]
    print("All test cases passed")


if __name__ == '__main__':
    move_zeros_test()
