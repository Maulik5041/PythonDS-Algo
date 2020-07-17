"""Find the next greater value than the current value or else return -1"""


class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def get_stack(self):
        if self.is_empty():
            return

        return self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return

        return self.items[-1]


def next_great(arr):

    if not arr or len(arr) == 1:
        return arr

    res = [-1] * len(arr)
    stack = Stack()

    for elem_index in range(len(arr) - 1, -1, -1):

        if not stack.is_empty():

            while not stack.is_empty() and stack.peek() <= arr[elem_index]:
                stack.pop()

        if not stack.is_empty():
            res[elem_index] = stack.peek()

        stack.push(arr[elem_index])

    return res


# O(n) time complexity
print(next_great([4, 6, 3, 2, 8, 1]))
print(next_great([10, 3, 7, 0, 12, 11, 2, 20, 1]))
