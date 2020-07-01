"""Output the unique pairs from the array to adds up to the given key"""


def pair_sum(an_array, key):

    if (not an_array) or (len(an_array) <= 1) or (not key):
        return None

    seen = set()
    pairs = set()

    for a_value in an_array:
        target = key - a_value

        if target in seen:
            pairs.add((min(a_value, target), max(a_value, target)))
        else:
            seen.add(a_value)

    print('\n'.join(map(str, list(pairs))))
    return len(pairs)


def pair_sum_test():

    assert pair_sum([], 3) is None
    assert pair_sum(None, 10) is None
    assert pair_sum([1, 2, 3], None) is None
    assert pair_sum([1, 3, 2, 2], 4) == 2
    assert pair_sum([3, 7, 2, 1, 0], 3) == 2
    assert pair_sum([2, 2, 2, 2], 4) == 1


if __name__ == '__main__':
    pair_sum_test()
    print("All tests passed")
