"""Counting the number of edges in an undirected graph"""


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
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)
    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


def num_edges_iteration(g):
    sum_up = 0
    for i in range(g.vertices):
        temp = g.array[i].head_node
        while temp is not None:
            sum_up += 1
            temp = temp.next_element
    return sum_up//2


def num_edges_recursion(g):
    return sum([g.array[i].length() for i in range(g.vertices)]) // 2


g = Graph(9)
g.add_edge(0, 2)
g.add_edge(0, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(6, 7)
g.add_edge(6, 8)
g.add_edge(6, 4)
g.add_edge(7, 8)

g2 = Graph(7)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(3, 4)
g2.add_edge(3, 5)
g2.add_edge(2, 5)
g2.add_edge(2, 4)
g2.add_edge(4, 6)
g2.add_edge(4, 5)
g2.add_edge(6, 5)

print(">>>>>>>>Iteration<<<<<<<")
print(num_edges_iteration(g))
print(num_edges_iteration(g2), "\n")
print(">>>>>>>>Recursion<<<<<<<")
print(num_edges_recursion(g))
print(num_edges_recursion(g2), "\n")
