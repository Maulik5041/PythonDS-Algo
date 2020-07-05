"""Given a dictionary of words and an input string tell whether the input
string can be completely segmented into dictionary words"""


def segment_string(a_str, a_dict):

    for a_char in range(1, len(a_str) + 1):
        first = a_str[0:a_char]

        if first in a_dict:
            second = a_str[a_char:]

            if (not second) or (second in a_dict) or segment_string(second, a_dict):
                return True

    return False


def segment_str_dp(a_str, a_dict):

    ok = [True]
    max_len = max(map(len, a_dict+['']))
    a_dict = set(a_dict)

    for a_char in range(1, len(a_str) + 1):

        ok += any(ok[j] and a_str[j:a_char] in a_dict for j in range(max(0, a_char - max_len), a_char))

    return ok[-1]


def segment_str_dp2(a_str, a_dict):

    length = len(a_str)
    memo = [False for i in range(length+1)]
    memo[0] = True

    for idx in range(length):

        if memo[idx]:

            for a_word in a_dict:
                word_len = len(a_word)

                if idx + word_len <= length and a_str[idx:idx+word_len] == a_word:
                    memo[idx+word_len] = True

    return memo[length]


