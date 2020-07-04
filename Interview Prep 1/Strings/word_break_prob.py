"""Given a dictionary of words and an input string tell whether the input
string can be completely segmented into dictionary words"""


def segment_str(a_str, dictionary):

    for an_idx in range(1, len(a_str) + 1):
        first = a_str[0:an_idx]

        if first in dictionary:
            second = a_str[an_idx:]

            if not second or second in dictionary or segment_str(second, dictionary):
                return True
    return False


s = "hellonow"
dictionary = set(["hello", "hell", "on", "now"])
if segment_str(s, dictionary):
    print("String Can be Segmented")
else:
    print("String Can NOT be Segmented")
