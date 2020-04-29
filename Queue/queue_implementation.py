"""Implementation of Queue in Python"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

print(q.size())
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)

print(q.size())

print(q.dequeue())
print(q.size())

print(q.dequeue())

print(q.size())

print(q.isEmpty())
