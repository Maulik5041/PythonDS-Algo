"""Find the maximum profit or minimum loss for buying a stock"""


def find_profit(array):

    if array is None or len(array) < 2:
        return None

    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy

    current_profit = float('-inf')

    for i in range(1, len(array)):
        current_profit = array[i] - current_buy

        if global_profit < current_profit:
            global_profit = current_profit
            global_sell = array[i]

        if array[i] < current_buy:
            current_buy = array[i]

    # result = global_sell - global_profit, global_sell

    return global_profit


def find_profit_test():

    assert find_profit(None) is None
    assert find_profit([2]) is None
    assert find_profit([21, 12, 4, 3, 0]) == -1
    assert find_profit([3, 4, 8, 0, 9, 10, 11, 45]) == 45
    assert find_profit([5, 4, 3, 2, 1]) == -1
    print("All test cases passed")


if __name__ == '__main__':
    find_profit_test()
