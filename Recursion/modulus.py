"""
Implementing mod operator
General formula: dividend mod divisor = (dividend - divisor) mod divisor
"""


def mod_op(dividend, divisor):
    if divisor == 0:
        print("Divisor cannot be")
        return 0

    if dividend < divisor:
        return dividend

    else:
        return mod_op(dividend - divisor, divisor)


def test_mod():
    assert mod_op(10, 4) == 2
    assert mod_op(10, 0) == 0
    assert mod_op(10, 10) == 0


if __name__ == '__main__':
    test_mod()
    print("Everything passed")
