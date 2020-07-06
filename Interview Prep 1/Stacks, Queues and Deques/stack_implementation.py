"""Implementation of Stack"""


class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        if self.is_empty():
            return

        return self.stack[-1]

    def pop(self):
        if self.is_empty():
            return

        return self.stack.pop()


st = Stack()
st.push(2)
st.push(5)
st.push(7)
st.push(1)
st.push(-3)

print("Size = ", st.size())
print("Peek = ", st.peek())

print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())

print("Size again = ", st.size())
print("Peek again = ", st.peek())

st.pop()
print("Peek finally = ", st.peek())
