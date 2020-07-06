"""Implement permutation of k items out of n items.
BAcktracking only visit each state once: O(|V|+|E|)"""


def a_n_k(a, n, k, depth, used, curr, ans):
    """
    :param depth: start from 0 and represent the depth of the search
    :param used: track what items are in the partial sol from set of n
    :param curr: the current partial solution
    :param ans: collect all the valid solutions
    """

    # end condition
    if depth == k:

        # use deepcopy because curr is tracking all partial solution
        # and it eventually becomes []
        ans.append(curr[::])

    for i in range(n):

        if not used[i]:

            # generate the next solution from curr
            curr.append(a[i])
            used[i] = True
            print(curr)

            # move to the next solution
            a_n_k(a, n, k, depth+1, used, curr, ans)

            # backtrack to the previous partial state
            curr.pop()
            print(f'Backtrack: {curr}')

            used[i] = False

    return


a = [1, 2, 3]
n = len(a)
ans = [[None]]
used = [False] * n
ans = []
a_n_k(a, n, n, 0, used, [], ans)
print(ans)
