"""Given a set of distinct integers, nums, return all possible subsets (the power set)"""


def subsets(nums):
    """
    :param nums: List[int]
    """

    # global list where we append every time the result
    result = []

    def dfs(temp, idx):

        # pass temp[:] with shallow copy so that the
        # result is not changed when temp is changed
        result.append(temp[:])

        for i in range(idx, len(nums)):

            print(f"i = {i}, temp = {temp}, idx = {idx}, result = {result}")

            temp.append(nums[i])
            dfs(temp, i+1)

            # Back track
            temp.pop()

    dfs([], 0)
    return result


(subsets([4, 2, 3]))
