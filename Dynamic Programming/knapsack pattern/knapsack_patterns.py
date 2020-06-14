"""Knapsack different patterns"""


# Method 1: Brute Force
def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_recursive(profits, weights, capacity - weights[current_index], current_index + 1)

    profit2 = knapsack_recursive(profits, weights, capacity, current_index + 1)

    return max(profit1, profit2)


print("Brute Force")
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


# Method 2: Memoization (Top-Down approach)
def solve_knapsack_memo(profits, weights, capacity):
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return recursive_knapsack(dp, profits, weights, capacity, 0)


def recursive_knapsack(dp, profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0

    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + recursive_knapsack(dp, profits, weights, capacity - weights[current_index], current_index + 1)

    profit2 = recursive_knapsack(dp, profits, weights, capacity, current_index + 1)

    dp[current_index][capacity] = max(profit1, profit2)
    return dp[current_index][capacity]


print("Memoization")
print(solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack_memo([1, 6, 10, 16], [1, 2, 3, 5], 6))
