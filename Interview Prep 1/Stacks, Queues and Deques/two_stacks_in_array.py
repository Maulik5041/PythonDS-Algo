"""Implement two stacks in an array"""


import numpy as np


class TwoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = np.zeros([n], dtype=int)
        self.top1 = -1
        self.top2 = self.size

    def push1(self, val):

        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = val

        else:
            print("Stack Overflow ")
            exit(1)

    def push2(self, val):

        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = val

        else:
            print("Stack Overflow ")
            exit(1)

    def pop1(self):

        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1

        else:
            print("Stack Overflow ")
            exit(1)

    def pop2(self):

        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1

        else:
            print("Stack Overflow ")
            exit(1)

    def get_stack(self):
        return self.arr


stack = TwoStacks(10)

print(stack.get_stack())

stack.push1(10)
stack.push1(12)
stack.push1(9)

stack.push2(-1)
stack.push2(-10)
stack.push2(0)

print(stack.get_stack())

stack.pop1()
stack.pop1()

stack.pop2()
stack.pop2()
stack.pop2()

print(stack.get_stack())

# stack.pop1()
stack.pop1()

# stack.pop2()

stack.push1(1000)

print("After popping a few values, the top element changes and by pushing 1000:")
print(stack.get_stack())
