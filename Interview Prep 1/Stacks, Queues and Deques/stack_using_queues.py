"""Implement a stack using Queue data structure"""


from collections import deque


class StackUsingQueue_1:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, data):
        self.queue1.append(data)

    def size(self):
        return len(self.queue1) + len(self.queue2)

    def is_empty(self):
        return self.size() == 0

    def swap_queues(self):
        self.queue3 = self.queue1
        self.queue1 = self.queue2
        self.queue2 = self.queue3

    def pop(self):
        if self.is_empty():
            return -1

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        value = self.queue1.popleft()
        self.swap_queues()
        return value


# Pop operation takes linear time
# as we are swapping elements between
# two queues.

# Push operation takes constant time
sq = StackUsingQueue_1()

print(f"Pop(): {str(sq.pop())}")

sq.push(3)
sq.push(5)
sq.push(9)

print(f"Pop(): {str(sq.pop())}")

sq.push(10)
sq.push(16)

print(f"Pop(): {str(sq.pop())}")


class StackUsingQueue_2:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def size(self):
        return len(self.queue1) + len(self.queue2)

    def is_empty(self):
        return self.size() == 0

    def push(self, data):

        if len(self.queue1) == 0:
            self.queue1.append(data)

        else:
            self.queue2.append(data)

            while len(self.queue1) != 0:
                self.queue2.append(self.queue1.popleft())
            self.swap_queues()

    def pop(self):

        if self.is_empty():
            return -1

        return self.queue1.popleft()

    def swap_queues(self):

        self.queue3 = self.queue1
        self.queue1 = self.queue2
        self.queue2 = self.queue1


# Push operation takes linear time
# as we are swapping elements between
# two queues.

# Pop operation takes constant time
sq2 = StackUsingQueue_2()

print(f"Pop(): {str(sq2.pop())}")

sq2.push(3)
sq2.push(5)
sq2.push(9)

print(f"Pop(): {str(sq2.pop())}")

sq2.push(10)
sq2.push(16)

print(f"Pop(): {str(sq2.pop())}")
