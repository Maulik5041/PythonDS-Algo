"""summing up the numbers from 1 to n"""


def sum_till(target_number):
    # Base Case
    if target_number == 1:
        return target_number

    else:
        return target_number + sum_till(target_number - 1)


if __name__ == '__main__':
    print(sum_till(20))
