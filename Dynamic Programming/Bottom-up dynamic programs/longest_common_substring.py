"""Finding longest common substring between two strings by different methods"""


# Simple Recursion: O(3^(m+n)) Exponential complexity
def lcs_recursion(str1, str2):
    return lcs_(str1, str2, 0, 0, 0)


def lcs_(str1, str2, i, j, count):
    if i >= len(str1) or j >= len(str2):
        return count

    if str1[i] == str2[j]:
        count = lcs_(str1, str2, i+1, j+1, count+1)

    return max(count, lcs_(str1, str2, i+1, j, 0), lcs_(str1, str2, i, j+1, 0))


print("Recursion")
print(lcs_recursion("hello", "elf"), "\n")


# Top-down approach: O(mn^2), m = size of str1, n = size of str2
def lcs_memoize(str1, str2):
    memo = {}
    return mem_helper(str1, str2, 0, 0, 0, memo)


def mem_helper(str1, str2, i, j, count, memo):
    if i >= len(str1) or j >= len(str2):
        return count

    if (i, j, count) in memo:
        return memo[(i, j, count)]

    c = count

    if str1[i] == str2[j]:
        c = mem_helper(str1, str2, i+1, j+1, count+1, memo)

    memo[(i, j, count)] = max(c, mem_helper(str1, str2, i+1, j, 0, memo), mem_helper(str1, str2, i, j+1, 0, memo))
    return memo[(i, j, count)]


print("Top-Down")
print(lcs_memoize("hel", "elf"), "\n")


# testing with longer strings
import random
import string


st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(40))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(60))
print(lcs_memoize(st1, st2+st1))


# Bottom-up approach: O(nm)
def lcs_tabulation(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    max_length = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    return max_length


print("Bottom-up")
print(lcs_tabulation("hel", "elf"), "\n")


strs1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(400))
strs2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(600))
print(lcs_tabulation(st1, strs2+strs1))


# Bottom-up approach with space optimization: Space = O(n)
def lcs_tabulation_opt(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [0 for i in range(n+1)]
    max_length = 0

    for j in range(1, m+1):
        this_row = [0 for i in range(n+1)]
        for i in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                this_row[i] = dp[i-1] + 1
                max_length = max(max_length, this_row[i])
            else:
                this_row[i] = 0
        dp = this_row
    return max_length


print("Bottom-up with space optimization")
print(lcs_tabulation_opt("hel", "elf"), "\n")


strs1_1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(400))
strs2_1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(600))
print(lcs_tabulation_opt(st1, strs2_1+strs1_1))
