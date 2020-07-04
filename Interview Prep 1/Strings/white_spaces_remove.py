"""Removing white spaces from a string in-place"""


def remove_whites(a_str):

    if not a_str:
        return

    a_str = ''.join([a_str[i] for i in range(len(a_str)) if a_str[i] != ' '])

    return a_str


print(remove_whites("Hi there"))
