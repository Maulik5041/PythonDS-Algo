"""Power of a number using Recursion"""


def power(base, exponent):
    if exponent == 0:
        return 1

    else:
        return base * power(base, exponent - 1)


if __name__ == '__main__':
    print(power(2, 3))
