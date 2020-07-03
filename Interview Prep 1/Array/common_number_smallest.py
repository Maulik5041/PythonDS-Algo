"""Find the smallest common number from the given sorted arrays"""


def smallest_num(l1, l2, l3):

    if not l1 or not l2 or not l3:
        return -1

    if l1 == l2 == l3:
        return l1[0]

    i = j = k = 0

    while i <= len(l1) and j <= len(l2) and k <= len(l3):

        if l1[i] == l2[j] == l3[k]:
            return l1[i]

        if l1[i] <= l2[j] and l1[i] <= l3[k]:
            i += 1

        elif l2[j] <= l1[i] and l2[j] <= l3[k]:
            j += 1

        elif l3[k] <= l1[i] and l3[k] <= l2[j]:
            k += 1

    return -1


def smallest_num_test():

    v1 = [6, 7, 10, 25, 30, 63, 64]
    v2 = [1, 4, 5, 6, 7, 8, 50]
    v3 = [1, 6, 10, 14]

    assert smallest_num(None, [], []) == -1
    assert smallest_num([], [], [1]) == -1
    assert smallest_num([], [], []) == -1
    assert smallest_num([1, 2, 3], [1, 2, 3], [1, 2, 3]) == 1
    assert smallest_num(v1, v2, v3) == 6
    print("All test cases passed")


if __name__ == '__main__':
    smallest_num_test()
