"""Finding the mother vertex of the directed graph"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        if(self.is_empty()):
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node


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
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        return front


class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for i in range(self.vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].insert_at_head(destination)


def find_mother_vertex_brute(g):
    num_of_vertices = 0
    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS_brute(g, i)
        if num_of_vertices_reached == g.vertices:
            return i

    return -1


def perform_DFS_brute(g, source):
    num_of_vertices = g.vertices
    vertices_reached = 0

    visited = [False] * num_of_vertices

    stack = Stack()
    stack.push(source)
    visited[source] = True

    while stack.is_empty() is False:
        curr = stack.pop()
        temp = g.array[curr].head_node
        while temp is not None:
            if visited[temp.data] is False:
                stack.push(temp.data)
                visited[temp.data] = True
                vertices_reached += 1
            temp = temp.next_element

    return vertices_reached + 1


def find_mother_vertex(g):
    visited = [False] * g.vertices
    last_v = 0
    for i in range(g.vertices):
        if visited[i] is False:
            perform_DFS(g, i, visited)
            last_v = i

    visited = [False] * g.vertices
    perform_DFS(g, last_v, visited)
    if any(i is False for i in visited):
        return -1
    return last_v


def perform_DFS(g, node, visited):
    visited[node] = True
    temp = g.array[node].head_node
    while temp:
        if visited[temp.data] is False:
            perform_DFS(g, temp.data, visited)
        temp = temp.next_element


g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(3, 0)
g1.add_edge(3, 1)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 0)
g.add_edge(3, 1)

print(find_mother_vertex(g))
print(find_mother_vertex_brute(g1))
