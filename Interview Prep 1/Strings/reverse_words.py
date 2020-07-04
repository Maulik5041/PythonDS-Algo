"""Reverse the order of words in a given sentence"""


from array import array
import sys


def get_array(a_atr):

    if not a_atr:
        return

    arr_str = array('u', a_atr)
    return arr_str


def reverse_words(a_sentence):

    if not a_sentence:
        return

    str_len = len(a_sentence)
    str_rev(a_sentence, 0, str_len - 1)

    start = 0
    end = 0

    while True:

        while start < str_len and a_sentence[start] == ' ':
            start += 1

        if start == str_len:
            break

        end = start + 1

        while end < str_len and a_sentence[end] != ' ':
            end += 1

        str_rev(a_sentence, start, end - 1)
        start = end

    return a_sentence


def str_rev(sentence, start, end):

    if not sentence or len(sentence) < 2:
        return

    while start < end:
        temp = sentence[start]
        sentence[start] = sentence[end]
        sentence[end] = temp
        start += 1
        end -= 1


def print_array(s):

    i = 0
    while i != len(s):
        sys.stdout.write(s[i])
        i += 1
    print()


def reverse_words_test():

    # The output is returned in an array form
    # But essentially all the sentences have been reversed
    assert reverse_words(get_array("")) is None
    assert reverse_words(get_array("Hi! My name is Tom.")) == array('u', 'Tom. is name My Hi!')
    assert reverse_words(get_array("Soldier!")) == array('u', 'Soldier!')
    assert reverse_words(get_array("A b cd EFG HijK Lm Nop 109")) == array('u', '109 Nop Lm HijK EFG cd b A')
    assert reverse_words(get_array(None)) is None
    print("All test cases passed")


if __name__ == '__main__':
    # print(reverse_words(get_array("")))
    # print(reverse_words(get_array("Hi! My name is Tom.")))
    # print(reverse_words(get_array("Soldier!")))
    # print(reverse_words(get_array("A b cd EFG HijK Lm Nop 109")))
    # print(reverse_words(get_array(None)))
    reverse_words_test()
