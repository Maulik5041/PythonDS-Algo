"""Check if the given two strings are anagram"""


def anagram(str_1, str_2):

    if str_1 and str_2:
        str_1 = str_1.lower().replace(" ", "")
        str_2 = str_2.lower().replace(" ", "")

    if not str_1 and not str_2:
        return True

    if (not str_1 and str_2) or (not str_2 and str_1) or (len(str_1) != len(str_2)):
        return False

    str_count = dict()

    for a_char in str_1:

        if a_char in str_count:
            str_count[a_char] += 1

        else:
            str_count[a_char] = 1

    for a_char in str_2:

        if a_char not in str_count:
            return False

        if a_char in str_count:
            str_count[a_char] -= 1

    for a_value in str_count.values():

        if a_value != 0:
            return False

    return True


def anagram_tests():
    assert anagram('dog', 'G O d') is True
    assert anagram(None, 'Hi') is False
    assert anagram(None, None) is True
    assert anagram('Coming', 'goinG') is False
    assert anagram('Clint Eastwood', 'Old WEST ACtion') is True
    assert anagram('aa', 'ab') is False


if __name__ == '__main__':
    anagram_tests()
    print("All tests passed")
