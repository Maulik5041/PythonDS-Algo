"""Find out if an undirected graph is a tree"""


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

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length


class MyQueue:
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


class MyStack:
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
        if (source < self.vertices) and (destination < self.vertices):
            self.array[source].insert_at_head(destination)
            self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List Model Undirected Graph<<")

        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1) is True:
        return False

    # Check if all nodes we visited from the source
    # i.e. the graph is connected
    for i, _ in enumerate(visited):
        # graph is not connected
        if visited[i] is False:
            return False
    # not cycle and is not connected
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, node) is True:
                return True

        elif adjacent.data is not parent:
            return True

        adjacent = adjacent.next_element

    return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)


print(is_tree(g))
