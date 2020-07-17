"""Evaluate a postfix expression"""


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


def eval_postfix_exp(exp):

    if not exp or (not exp[0].isdigit() and not exp[1].isdigit()):
        return None

    temp_stack = Stack()
    try:
        for a_char in exp:

            if a_char.isdigit():
                temp_stack.push(a_char)

            else:
                val2 = temp_stack.pop()
                val1 = temp_stack.pop()
                temp_stack.push(str(eval(val1 + a_char + val2)))

    except TypeError:
        return "Invalid Sequence"

    return int(float(temp_stack.pop()))


print(eval_postfix_exp("921*-8-4+"))
print(eval_postfix_exp("921*-8--4+"))
