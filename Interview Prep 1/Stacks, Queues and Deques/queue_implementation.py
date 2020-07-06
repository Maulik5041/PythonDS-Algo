"""Implement a Queue"""


class Queue:

    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if self.is_empty():
            return

        return self.queue.pop()


q = Queue()

print(f"Size = {q.size()}")

q.enqueue(-1)
q.enqueue(78)
q.enqueue(0)
q.enqueue(34)

print(f"Dequeue = {q.dequeue()}")
print(f"Dequeue = {q.dequeue()}")

q.enqueue(100)
q.enqueue(-45)

print(f"Dequeue = {q.dequeue()}")
print(f"Dequeue = {q.dequeue()}")
print(f"Dequeue = {q.dequeue()}")
print(f"Dequeue = {q.dequeue()}")

print(f"Size = {q.size()}")
