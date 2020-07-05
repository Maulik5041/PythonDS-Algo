"""Find all substrings in a given string that are palindromes"""


# Method 1: Time = O(N^3) and Space = O(1)
def find_all_pal_subs(inp):

    if not inp or len(inp) == 1:
        return False

    count = 0

    for a_char in range(0, len(inp)):
        for other_chars in range(a_char+1, len(inp)):
            if is_palindrome(inp, a_char, other_chars):
                print(inp[a_char:other_chars+1])
                count += 1
    return count


def is_palindrome(inp, i, j):

    while j > i:
        if inp[i] != inp[j]:
            return False

        i += 1
        j -= 1

    return True


# Method 2: O(N^2) and Space = O(1)
def find_all_pal_subs_2(inp):

    if not inp or len(inp) == 1:
        return False

    count = 0

    for a_char in range(0, len(inp)):

        count += find_pals_in_string(inp, a_char-1, a_char+1)
        count += find_pals_in_string(inp, a_char, a_char+1)

    return count


def find_pals_in_string(inp, j, k):
    count = 0

    while j >= 0 and k < len(inp):
        if inp[j] != inp[k]:
            break

        print(inp[j:k+1])
        count += 1

        j -= 1
        k += 1

    return count


def palindrome_tests():

    assert find_all_pal_subs("") is False
    assert find_all_pal_subs("a") is False
    assert find_all_pal_subs("Aaz") == 0
    assert find_all_pal_subs("aabbbaa") == 7
    print("All test cases passed in first approach")

    assert find_all_pal_subs_2("") is False
    assert find_all_pal_subs_2("a") is False
    assert find_all_pal_subs_2("Aaz") == 0
    assert find_all_pal_subs_2("aabbbaa") == 7
    print("All test cases passed in second appraoch")


if __name__ == '__main__':
    palindrome_tests()
