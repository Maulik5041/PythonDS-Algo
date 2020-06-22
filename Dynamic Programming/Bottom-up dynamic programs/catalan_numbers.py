"""Catalan numbers solutions"""


# Recursion: O(n!) Factorial complexity
def catalan_recursion(n):
    if n == 0:
        return 1

    sum_val = 0

    for i in range(n):
        sum_val += catalan_recursion(i) * catalan_recursion(n - 1 - i)
    return sum_val


print(catalan_recursion(4))


# Top-down Memoization: O(n^2) quadratic complexity
def catalan_memoize(n):
    memoize = {}
    return helper_catalan(n, memoize)


def helper_catalan(n, memoize):
    if n == 0:
        return 1

    elif n in memoize:
        return memoize[n]

    sum_val = 0

    for i in range(n):
        sum_val += helper_catalan(i , memoize) * helper_catalan(n - 1 - i, memoize)

    memoize[n] = sum_val
    return memoize[n]


print(catalan_memoize(400))


# Bottom-up approach: O(n^2)
def catalan_tabulation(n):
    table = [None] * (n+1)
    table[0] = 1

    for i in range(1, n + 1):
        table[i] = 0

        for j in range(i):
            table[i] += table[j] * table[i - j - 1]
    return table[n]


print(catalan_tabulation(1000))
