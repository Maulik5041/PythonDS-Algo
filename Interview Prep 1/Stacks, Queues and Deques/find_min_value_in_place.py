"""Implement a class that gets the minimum value in constant time"""


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


class MinStack:

    def __init__(self):
        self.main_stack = Stack()
        self.min_stack = Stack()
        return

    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    def push(self, item):

        self.main_stack.push(item)

        if self.min_stack.is_empty() or self.min_stack.peek() >= item:
            self.min_stack.push(item)
        else:
            self.min_stack.push(self.min_stack.peek())

    def push1(self, item):
        self.main_stack.push(item)

        if self.min_stack.size() == 0:
            self.min_stack.push(item)

        curr = self.min_stack.pop()
        self.tmp_stack = Stack()
        self.tmp_stack.push(curr)

        while item > curr and self.min_stack.size() > 0:
            curr = self.min_stack.pop()
            self.tmp_stack.push(curr)

        if curr > item:
            self.min_stack.push(self.tmp_stack.pop())

        self.min_stack.push(item)
        while self.tmp_stack.size() > 0:
            self.min_stack.push(self.tmp_stack.pop())

    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()


stack = MinStack()

# This method gives the overall minimum
# will not update the stack until a
# smaller value is pushed
stack.push(5)
stack.push(0)
stack.push(2)
stack.push(4)
stack.push(1)
stack.push(3)
stack.push(0)

# This method gives more accurate result
# it pushes all the values to min stack
# with actual minimum value at the top
stack.push1(10)
stack.push1(3)
stack.push1(23)
stack.push1(37)
stack.push1(15)
stack.push1(30)
stack.push1(1)

print(stack.main_stack.items, "\n")
print("Minimum stack looks like this")
print(stack.min_stack.items, "\n")
print(stack.min())

stack.pop()
stack.pop()

print("\nMinimum stack after popping twice")
print(stack.min_stack.items, "\n")

print(stack.main_stack.items)
print(stack.min())
