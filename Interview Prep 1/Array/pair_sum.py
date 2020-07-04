"""Find pair with given sum in an array"""


def find_two_sum(array, sum_val):

    if not array:
        return None

    pair_val = set()

    for i in array:

        if sum_val - i in pair_val:
            return True, ((sum_val - i), i)

        pair_val.add(i)

    return False


# print(find_two_sum([5, 7, 1, 2, 8, 4, 3], 10))
def find_two_sum_test():

    assert find_two_sum([5, 7, 1, 2, 8, 4, 3], 10) == (True, (2, 8))
    assert find_two_sum([5, 7, 1, 2, 8, 4, 3], 19) is False
    assert find_two_sum([], 12) is None
    assert find_two_sum([1, 2, 3, 4, 5, 6], 7) == (True, (3, 4))
    print("All test cases passed")


if __name__ == '__main__':
    find_two_sum_test()
