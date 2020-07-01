"""Reverse the given sentence and remove the leading and trailing spaces"""


def rev_words(str_1):

    if not str_1:
        return

    words = []
    length = len(str_1)
    space = [' ']

    idx = 0

    while idx < length:

        if str_1[idx] not in space:

            word_start = idx

            while idx < length and str_1[idx] not in space:

                idx += 1

            words.append(str_1[word_start:idx])

        idx += 1

    return ' '.join(words[::-1])


def rev_words_test():
    assert rev_words("   ") == ""
    assert rev_words(None) is None
    assert rev_words("  Howdy! Life is good   ") == "good is Life Howdy!"
    assert rev_words(" Here I go !") == "! go I Here"
    assert rev_words("I") == "I"
    assert rev_words(" 9 o p klk A . m _   ") == "_ m . A klk p o 9"


if __name__ == '__main__':
    rev_words_test()
    print('All test cases passed')
