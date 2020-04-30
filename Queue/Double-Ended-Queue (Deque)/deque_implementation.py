"""Implementation of double ended queue DS in Python"""


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        return self.items.append(item)

    def add_rear(self, item):
        return self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.is_empty())

print("Adding 4 and dog at the rear end")
d.add_rear(4)
d.add_rear('dog')
print(d.size())

print("Adding cat and True at the front end")
d.add_front('cat')
d.add_front(True)
print(d.size())
print(d.is_empty())


d.add_rear(8.4)

print("Removing from the rear")
print(d.remove_rear())

print("Removing from the front")
print(d.remove_front())

print(d.size())