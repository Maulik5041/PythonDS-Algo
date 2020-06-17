"""Implementing gcd between two variables using recursion"""


def gcd(test_variable_1, test_variable_2):
    if test_variable_1 == test_variable_2:
        return test_variable_1

    if test_variable_1 > test_variable_2:
        return gcd(test_variable_1 - test_variable_2, test_variable_2)
    return gcd(test_variable_1, test_variable_2 - test_variable_1)


def test_gcd():
    assert gcd(10, 8) == 2
    assert gcd(9, 5) == 1
    assert gcd(1000, 10) == 10
    assert gcd(3563, 13) == 1


if __name__ == "__main__":
    test_gcd()
    print("Successful Tests")
