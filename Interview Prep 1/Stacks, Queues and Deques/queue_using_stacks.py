"""Implement a queue using stacks"""


# Unlike in implementing a stack, here
# we don't need to swap stacks. The two
# stacks works together to run queue operation
class QueueUsingStack_1:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if self.is_empty():
            return -1

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                # val = self.stack1[-1]
                self.stack2.append(self.stack1.pop())

        val = self.stack2[-1]
        self.stack2.pop()
        return val


# Enqueue operation takes constant time
# Dequeue operation takes linear time as
# it moves elements from Stack1 -> Stack2
qs_1 = QueueUsingStack_1()

qs_1.enqueue(3)
qs_1.enqueue(7)
qs_1.enqueue(10)

print(f"Dequeue(): {str(qs_1.dequeue())} --> 3?")

qs_1.enqueue(4)
qs_1.enqueue(90)

print(f"Dequeue(): {str(qs_1.dequeue())} --> 7?")

qs_1.enqueue(-1)
qs_1.enqueue(135)

print(f"Dequeue(): {str(qs_1.dequeue())} --> 10?")
print(f"Dequeue(): {str(qs_1.dequeue())} --> 4?")
print(f"Dequeue(): {str(qs_1.dequeue())} --> 90?")
print(f"Dequeue(): {str(qs_1.dequeue())} --> -1?")


class QueueUsingStack_2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        if len(self.stack1) == 0:
            self.stack1.append(data)

        else:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

            self.stack1.append(data)

            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return -1

        return self.stack1.pop()


# Enqueue operation takes linear time
# Dequeue operation takes constant time
qs_2 = QueueUsingStack_2()

qs_2.enqueue(3)
qs_2.enqueue(7)
qs_2.enqueue(10)

print(f"Dequeue(): {str(qs_2.dequeue())} --> 3?")

qs_2.enqueue(4)
qs_2.enqueue(90)

print(f"Dequeue(): {str(qs_2.dequeue())} --> 7?")

qs_2.enqueue(-1)
qs_2.enqueue(135)

print(f"Dequeue(): {str(qs_2.dequeue())} --> 10?")
print(f"Dequeue(): {str(qs_2.dequeue())} --> 4?")
print(f"Dequeue(): {str(qs_2.dequeue())} --> 90?")
print(f"Dequeue(): {str(qs_2.dequeue())} --> -1?")
