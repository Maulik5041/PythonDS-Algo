"""Time Complexity = O(N * C)
   Space Complexity = O(N * C)
"""


def solve_knapsack(profits, weights, capacity):
    # create a two dimensional array for memoization
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, current_index):
    # Base checks
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # See if the solution is in the memory
    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]

    # Recursive call after choosing the current index
    # The weight of the current index should be lesser than the total capacity
    profit_1 = 0
    if weights[current_index] <= capacity:
    	profit_1 = profits[current_index] + knapsack_recursive(dp, profits, weights, capacity - weights[current_index], current_index + 1)

    # Recursive call after exclusing the current index
    profit_2 = knapsack_recursive(dp, profits, weights, capacity, current_index + 1)
    dp[current_index][capacity] = max(profit_1, profit_2)
    return dp[current_index][capacity]


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
