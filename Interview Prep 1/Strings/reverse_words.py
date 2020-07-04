"""Reverse the order of words in a given sentence"""


def reverse_words(sentence):

    # String is a null-terminated string
    # ending with char '\0'
    if not sentence:
        return

    # Reverse the entire string
    str_len = len(sentence)
    str_rev(sentence, 0, str_len - 2)

    # All the words are at required location
    # but verything is in reverse order
    # Iterate over the sentence and reverse words
    start = 0
    end = 0

    while True:

        # Find the start of a word while skipping spaces
        while start < str_len and sentence[start] == ' ':
            start += 1

        if start == str_len:
            break

        # Find the end of the word
        end = start + 1
        while end < str_len and sentence[end] != ' ':
            end += 1

        # Reversing the word in-place
        str_rev(sentence, start, end-1)
        start = end


def str_rev(sentence, start, end):

    if sentence is None or len(sentence) < 2:
        return

    while start < end:
        temp = sentence[start]
        sentence[start] = sentence[end]
        sentence[end] = temp

        start += 1
        end -= 1


def reverse_words_test():

    assert reverse_words("") is None
    assert reverse_words("Hi! My name is Tom.") == "Tom. is name My Hi!"
    assert reverse_words("Soldier!") == "Soldier!"
    assert reverse_words("A b cd EFG HijK Lm Nop 109") == "109 Nop Lm HijK EFG cd B A"
    assert reverse_words(None) is None
    print("All test cases passed")


if __name__ == '__main__':
    reverse_words_test()
