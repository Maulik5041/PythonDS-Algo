"""Time Complexity = O(N * C)
   Space Complexity = O(N ∗ C)
"""


def solve_knapsack(profits, weights, capacity):

    # Base checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # If only one weight and is less than the capacity then take it
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # Process all the sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit_1, profit_2 = 0, 0
            # Include the item if it is not more than the capacity
            if weights[i] <= c:
                profit_1 = profits[i] + dp[i - 1][c - weights[i]]

            # Exclude the item
            profit_2 = dp[i - 1][c]

            # Take maximum
            dp[i][c] = max(profit_1, profit_2)

    print_selected_elements(dp, weights, profits, capacity)
    # maximum profit will be at the bottom-right corner.
    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n-1][capacity]
    for i in range(n-1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
        print()


print(f"Total knapsack profit: {(str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))}")
print(f"Total knapsack profit: {(str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))}")
