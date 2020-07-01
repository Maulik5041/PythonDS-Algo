"""Compress the string"""


def string_compression1(str_1):
    """This method uses hash table to store values"""

    if not str_1:
        return

    if len(str_1) == 1:
        return str_1 + '1'

    count = dict()
    result = ''

    for a_char in str_1:

        if a_char not in count:

            count[a_char] = 1

        else:

            count[a_char] += 1

    for key, value in count.items():

        result += (str(key) + str(value))

    return result


def string_compression_2(str_2):
    """This method uses pointers to solve the problem"""

    if not str_2:
        return

    result = ''
    length = len(str_2)

    if length == 0:
        return

    if length == 1:
        return str_2 + '1'

    count = 1
    idx = 1

    while idx < length:

        if str_2[idx] == str_2[idx - 1]:
            count += 1

        else:
            result += (str_2[idx - 1] + str(count))
            count = 1

        idx += 1

    result += str_2[idx - 1] + str(count)

    return result


def string_compression_test():

    assert string_compression_2(None) is None
    assert string_compression_2("") is None
    assert string_compression_2("a") == "a1"
    assert string_compression_2("AAAbBBBccD") == "A3b1B3c2D1"
    assert string_compression_2("aaB") == "a2B1"
    assert string_compression_2("Tarzan") == "T1a1r1z1a1n1"


if __name__ == '__main__':
    string_compression_test()
    print("All test cases passed")
