"""Merge overlapping intervals in an array of interval pairs"""


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second


def merge_intervals(pairs):

    if not pairs:
        return None

    result = []
    result.append(Pair(pairs[0].first, pairs[0].second))

    for i in range(1, len(pairs)):

        x1 = pairs[i].first
        y1 = pairs[i].second

        x2 = result[len(result) - 1].first
        y2 = result[len(result) - 1].second

        if y2 >= x1:
            result[len(result) - 1].second = max(y1, y2)
        else:
            result.append(Pair(x1, y1))

    return result


p1 = [Pair(1, 5), Pair(3, 1), Pair(4, 6), Pair(6, 8), Pair(10, 12), Pair(11, 15)]

res = merge_intervals(p1)
for i in range(len(res)):
    print("[" + str(res[i].first) + ", " + str(res[i].second) + "]", end=" ")
