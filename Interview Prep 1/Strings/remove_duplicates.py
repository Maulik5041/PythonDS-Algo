"""Remove duplicates from the string"""


def remove_duplicates(a_string):

    if not a_string:
        return

    if len(a_string) == 1:
        return a_string

    found = ""

    for a_char in a_string:

        if a_char not in found:
            found += a_char

    return found


def remove_duplicates_test():

    assert remove_duplicates("absndjbakdg") == "absndjkg"
    assert remove_duplicates("") is None
    assert remove_duplicates("A") == "A"
    assert remove_duplicates("111122233445") == "12345"
    assert remove_duplicates("H-e-L-l-O W-o-R-L-d-!!") == "H-eLlO WoRd!"
    print("All test cases passed")


if __name__ == '__main__':
    remove_duplicates_test()


"""
The above approach is not an in-place removal. Rather it creates
another string of unique characters. To remove in-place, we need
two pointers. One of them keeps a track of unique characters
and other is to keep track of duplicate and write something on it.
Once the unique pointer reaches the end of the array, another pointer
should be somewhere in the array. Replace all the remaining characters
with None and so it would be considered removed.
"""
