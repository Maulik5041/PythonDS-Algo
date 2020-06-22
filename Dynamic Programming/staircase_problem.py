"""Recusrion method: O(m^n) exponential complexity"""


def staircase_rescursion(total_steps, biggest_leap):
    if total_steps == 0:
        return 1

    ways_to_climb = 0

    for a_leap in range(1, biggest_leap + 1):
        if a_leap <= total_steps:
            ways_to_climb += staircase_rescursion(total_steps - a_leap, biggest_leap)
    return ways_to_climb


print(staircase_rescursion(4, 2))


"""Memoization method: O(n) linear complexity"""


def staircase_memoization(total_steps, biggest_leap):
    memoize = {}
    return nth_stair(total_steps, biggest_leap, memoize)


def nth_stair(total_steps, biggest_leap, memoize):
    if total_steps == 0:
        return 1

    if total_steps in memoize:
        return memoize[total_steps]

    ways_to_climb = 0

    for a_step in range(1, biggest_leap + 1):
        if a_step <= total_steps:
            ways_to_climb += nth_stair(total_steps - a_step, biggest_leap, memoize)

    memoize[total_steps] = ways_to_climb
    return ways_to_climb


print(staircase_memoization(100, 6))
