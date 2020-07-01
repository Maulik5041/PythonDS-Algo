"""Check if all the characeters in a string are unique"""


def unique_chars(a_str):

    if not a_str:
        return False

    if a_str == " ":
        return True

    # A dictionary or a set could be used to store
    # count = dict()
    count = set()

    for a_char in a_str:

        if a_char in count:
            return False

        count.add(a_char)

    return True


def unique_chars_test():

    assert unique_chars(None) is False
    assert unique_chars(" ") is True
    assert unique_chars("") is False
    assert unique_chars("abcdeFGhi") is True
    assert unique_chars("aaGbnvhd") is False
    assert unique_chars("1223Abch") is False
    assert unique_chars(".amcbdheiwu") is True


if __name__ == '__main__':
    unique_chars_test()
    print("All test cases passed")
