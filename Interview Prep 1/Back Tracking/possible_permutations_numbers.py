"""Given a collection of distinct numbers, return all possible permutations"""


def permute(nums):
    """
    :param nums" List[int]
    """

    # global list that keeps track of all solutions
    result = []

    def dfs(temp, elements):

        # gather result
        if len(elements) == 0:
            result.append(temp[:])

        for e in elements:
            temp.append(e)

            # Back track
            next_elements = elements[:]
            next_elements.remove(e)

            elements.pop()
            dfs(temp, next_elements)
            temp.pop()

    # first is the current result
    dfs([], nums)
    return result


print(permute([1, 2, 3]))
