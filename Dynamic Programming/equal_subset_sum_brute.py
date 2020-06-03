def can_partition(num):
    s = sum(num)

    if s % 2 != 0:
        return 0

    return can_partition_recursive(num, s/2, 0)


def can_partition_recursive(num, sm, current_index):

    if sm == 0:
        return True

    n = len(num)
    if n == 0 or current_index >= n:
        return False

    if num[current_index] <= sm:
        if (can_partition_recursive(num, sm - num[current_index], current_index + 1)):
            return True

    return can_partition_recursive(num, sm, current_index + 1)


print("Can partition: " + str(can_partition([1, 2, 3, 4])))
print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
print("Can partition: " + str(can_partition([2, 3, 4, 6])))
