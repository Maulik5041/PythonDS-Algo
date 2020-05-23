"""Implemention of depth first search on a directed graph using adjacency list"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def enqueue(self, value):
        return self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue_list.remove(self.queue_list[0])


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

    def size(self):
        return len(self.stack_list)


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if not self.head:
            return True
        return False

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = None
            return self.head

        new_node.next = self.head
        self.head = new_node
        return self.head


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


def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result

    visited = []
    for i in range(num_of_vertices):
        visited.append(False)

    result, visited = dfs_traversal_helper(g, source, visited)

    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


def dfs_traversal_helper(g, source, visited):
    result = ""
    stack = Stack()
    stack.push(source)
    visited[source] = True

    while stack.is_empty() is False:
        curr = stack.pop()
        result += str(curr)
        temp = g.array[curr].head

        while temp is not None:
            if visited[temp.data] is False:
                stack.push(temp.data)
                visited[temp.data] = True
            temp = temp.next
    return result, visited


g = Graph(7)
num_of_vertices = g.vertices
if(num_of_vertices is 0):
    print("Graph is empty")
elif(num_of_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    print(dfs_traversal(g, 1))
