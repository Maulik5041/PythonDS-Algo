"""Implementation of the game hot-potato using a Queue DS in Python"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hot_potato(name_list, num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
