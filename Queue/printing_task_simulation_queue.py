"""Printing tasks in a lab using Queue DS in Python"""

import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulations(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_Queue = Queue()
    waitingtimes = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_Queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_Queue.is_empty()):
            next_task = print_Queue.dequeue()
            waitingtimes.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waitingtimes)/len(waitingtimes)
    print(f"Average wait {average_wait} secs {(print_Queue.size())} tasks remaining")


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulations(3600, 10)
