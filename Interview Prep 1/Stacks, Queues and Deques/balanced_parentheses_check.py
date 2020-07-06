"""Check if the given string of Parentheses are balanced"""


def are_balanced(left, right):

    if left == '(' and right == ')':
        return True

    if left == '{' and right == '}':
        return True

    if left == '[' and right == ']':
        return True

    return False


def check_brackets(a_str):

    if not a_str:
        return

    if len(a_str) % 2 != 0:
        return False

    stack = []

    opening_brackets = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    for a_bracket in a_str:

        if a_bracket in opening_brackets:
            stack.append(a_bracket)

        else:
            prev_bracket = stack.pop()

            if (prev_bracket, a_bracket) not in matches:
                return False

            # if not are_balanced(prev_bracket, a_bracket):
            #     return False

    return len(stack) == 0


# This problem can be solved by 2 ways:
# 1. By creating other method that checks balance of brackets
# 2. By creating a set of matches and comparing those tuples
def check_brackets_test():

    assert check_brackets("") is None
    assert check_brackets(None) is None
    assert check_brackets("((([[[]]])))") is True
    assert check_brackets(")()[]{}({})") is False
    assert check_brackets("({{}})[]{{()}}[(())]") is True
    assert check_brackets("((((((())))))") is False
    print("All test cases passed")


if __name__ == '__main__':
    check_brackets_test()
