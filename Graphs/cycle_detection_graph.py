"""Detect if the directed graph has a cycle or loop inside of it"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def enqueue(self, value):
        return self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.queue_list.remove(self.front())


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def push(self, value):
        return self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.stack_list.pop()


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def get_head(self):
        if self.is_empty():
            return None
        return self.head

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = None
            return self.head

        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = None
            return self.head

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        new_node.next = None
        return self.head

    def length(self):
        if self.is_empty():
            return None

        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next

        return count


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        if (source < self.vertices) and (destination < self.vertices):
            self.array[source].insert_at_head(destination)

    def print_graph(self):
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")


def detect_cycle(g):
    visited = [False] * g.vertices
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True

    return False


def detect_cycle_rec(g, node, visited, rec_node_stack):
    if rec_node_stack[node]:
        return True

    if visited[node]:
        return False

    visited[node] = True
    rec_node_stack[node] = True

    head = g.array[node].head
    while head is not None:
        adjacent = head.data
        if (detect_cycle_rec(g, adjacent, visited, rec_node_stack)):
            return True
        head = head.next

    rec_node_stack[node] = False
    return False


g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(3, 0)

g2 = Graph(3)
g2.add_edge(0, 1)
g2.add_edge(1, 2)

print(detect_cycle(g1))
print(detect_cycle(g2))
