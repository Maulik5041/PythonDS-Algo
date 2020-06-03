"""Time Complexity = O(2^n)
   Space Complexity = O(n)
"""


def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)


def knapsack_recursive(profits, weights, capacity, current_index):
    # Base checks
    if capacity <= 0 or current_index >= len(profits):
        return 0

    # Recursive call after choosing the current indexed element
    # The weight of the current index should not exceed the capacity
    profit_1 = 0
    if weights[current_index] <= capacity:
        profit_1 = profits[current_index] + knapsack_recursive(profits, weights, capacity - weights[current_index], current_index + 1)

    profit_2 = knapsack_recursive(profits, weights, capacity, current_index + 1)

    return max(profit_1, profit_2)


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
