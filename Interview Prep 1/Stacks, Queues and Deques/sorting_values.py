"""Sort values in a stack"""


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
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return

        return self.items[-1]


# Method 1: Iteration --> O(n^2)
def sort_stack_iter(stack):

    if stack.is_empty() or stack.size() == 1:
        return stack

    temp_stack = Stack()
    while not stack.is_empty():

        value = stack.pop()
        if temp_stack.peek() and value >= int(temp_stack.peek()):
            temp_stack.push(value)

        else:
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())
            temp_stack.push(value)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


print("\nSorting of stack by Iteration")
main_stack = Stack()
main_stack.push(63)
main_stack.push(2)
main_stack.push(90)
main_stack.push(4)
main_stack.push(27)
main_stack.push(42)
main_stack.push(3)

print(main_stack.get_stack())

sort_stack_iter(main_stack)

print(main_stack.get_stack(), "\n")


# Method 2: Recursion --> O(n^2)
def sorting_stack_recur(stack):

    if stack.is_empty() or stack.size() == 1:
        return stack

    if not stack.is_empty():

        value = stack.pop()
        sorting_stack_recur(stack)

        insert(stack, value)

    return stack


def insert(stack, value):

    if stack.is_empty() or value < stack.peek():
        stack.push(value)

    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)


print("\nSorting of stack by Recursion")
main_stack_2 = Stack()
main_stack_2.push(63)
main_stack_2.push(2)
main_stack_2.push(90)
main_stack_2.push(4)
main_stack_2.push(27)
main_stack_2.push(42)
main_stack_2.push(3)

print(main_stack_2.get_stack())

sorting_stack_recur(main_stack_2)

print(main_stack_2.get_stack(), "\n")


# Method 3: Simple Sorting --> O(nlogn)
def sort_stack(stack):

    stack.get_stack().sort(reverse=True)
    return stack


print("\nSorting of stack by simmple sorting")
main_stack_3 = Stack()
main_stack_3.push(63)
main_stack_3.push(2)
main_stack_3.push(90)
main_stack_3.push(4)
main_stack_3.push(27)
main_stack_3.push(42)
main_stack_3.push(3)

print(main_stack_3.get_stack())

sort_stack(main_stack_3)

print(main_stack_3.get_stack(), "\n")
