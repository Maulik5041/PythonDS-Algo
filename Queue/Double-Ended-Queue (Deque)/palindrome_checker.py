"""Using deque abstract data type to solve the palindrome problem"""


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


def pal_checker(a_string):
    chardeque = Deque()

    for ch in a_string:
        chardeque.add_rear(ch)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
