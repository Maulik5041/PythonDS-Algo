"""Implementing a double-ended queue (deque)"""


class Deque:

    def __init__(self):
        self.deque = []

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return self.size() == 0

    def add_rear(self, data):
        self.deque.insert(0, data)

    def add_front(self, data):
        self.deque.append(data)

    def remove_front(self):
        return self.deque.pop()

    def remove_rear(self):
        return self.deque.pop(0)


dq = Deque()

print(f"Size = {dq.size()}")

dq.add_front(2)
dq.add_front(5)

dq.add_rear(-1)
dq.add_rear(-5)

print(f"Size = {dq.size()}")

print(f"Removed from Front = {dq.remove_front()}")
print(f"Removed from Rear = {dq.remove_rear()}")

print(f"Size = {dq.size()}")

print(f"Removed from Rear = {dq.remove_rear()}")
print(f"Removed from Rear = {dq.remove_rear()}")

print(f"Size = {dq.size()}")
