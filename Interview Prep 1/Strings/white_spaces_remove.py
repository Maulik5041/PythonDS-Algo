"""Removing white spaces from a string in-place. This is
not possible in Python. This is just an exercise but is
more relevant for the lower level languages where adding
a null character can terminate the string at that point.
We will convert the string to an array class and try to
add this character just to get a feel of how it might work
in the languages that support this type of functionality"""


from array import array
import sys


def get_array(a_str):

    if not a_str:
        return

    arr_str = array('u', a_str)
    return arr_str


def print_array(a_str):

    if not a_str:
        return

    i = 0
    result = ""
    while i < len(a_str) and a_str[i] != '\x00':
        # sys.stdout.write(a_str[i])
        result += a_str[i]
        i += 1
    # print()
    return result


def remove_whites(a_str):

    if not a_str:
        return

    read_idx = 0
    write_idx = 0

    while read_idx < len(a_str):
        if a_str[read_idx] != '\t' and a_str[read_idx] != ' ':
            a_str[write_idx] = a_str[read_idx]
            write_idx += 1
        read_idx += 1

    a_str[write_idx] = '\x00'

    return a_str


def remove_whites_test():

    assert print_array(remove_whites(get_array(""))) is None
    assert print_array(remove_whites(get_array("1 2 3 3  4 5"))) == "123345"
    assert print_array(remove_whites(get_array(" Hello world! "))) == "Helloworld!"
    assert print_array(remove_whites(get_array("\t T h i s ss  is ho w IT is"))) == "ThisssishowITis"
    assert print_array(remove_whites(get_array("       "))) == ""
    print("All test cases passed")


if __name__ == '__main__':
    remove_whites_test()
