"""Remove duplicates from the string in-place.
In Python, strings are immutables and thus not
possible to update a string in-place. So instead,
we convert this string to an array class and give
it a termination character \\0, which is a null
character in a lower level language. If in an array,
this character is found, that is the end of the array
and essentially the original string"""


from array import array


def get_array(a_str):

    # Convert string to an array
    # so that it could be modified
    if not a_str:
        return

    arr_str = array('u', a_str)
    return arr_str


def print_array(a_str):

    if not a_str:
        return

    # Get the output of the 
    # reversed string.
    # Stop the loop once it
    # reaches the character \x00
    i = 0
    result = ""
    while i < len(a_str):
        # print(a_str[i])
        if a_str[i] == '\x00':
            break
        result += a_str[i]
        i += 1
    return result


def remove_duplicates(a_str):

    if not a_str:
        return

    if len(a_str) == 1:
        return a_str

    hashset = set([])
    write_idx = 0
    read_idx = 0

    while read_idx < len(a_str):
        if a_str[read_idx] not in hashset:
            hashset.add(a_str[read_idx])
            a_str[write_idx] = a_str[read_idx]
            write_idx += 1

        read_idx += 1

    a_str[write_idx] = '\x00'

    return a_str


def remove_duplicates_test():

    # 1. converting string to array class
    # 2. adding \x00 to partition between unique and
    #        duplicate characters
    # 3. getting the array class of the string
    #        only till the unique characters
    # NOTE: This method does not apply in Python as strings are immutable
    # This is just an exercise which is more relevant to lower level languages
    assert print_array(remove_duplicates(get_array("absndjbakdg"))) == "absndjkg"
    assert print_array(remove_duplicates(get_array(""))) is None
    assert print_array(remove_duplicates(get_array("A"))) == "A"
    assert print_array(remove_duplicates(get_array("111122233445"))) == "12345"
    assert print_array(remove_duplicates(get_array("H-e-L-l-O W-o-R-L-d-!!"))) == "H-eLlO WoRd!"
    print("All test cases passed")


if __name__ == '__main__':
    remove_duplicates_test()
