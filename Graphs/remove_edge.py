"""Removing an edge between the two vertices of a directed graph"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


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

    def delete_at_head(self):
        first_element = self.get_head()

        if first_element:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():
            print("List is Empty")
            return deleted

        curr = self.get_head()
        prev = None
        if curr.data == value:
            self.delete_at_head()
            deleted = True
            return deleted

        while curr:
            if value == curr.data:
                prev.next_element = curr.next_element
                curr.next_element = None
                deleted = True
                break
            prev = curr
            curr = curr.next_element
        return deleted


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

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)
    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


def remove_edge(graph, source, dest):
    if len(graph.array) == 0:
        return graph

    # check if source is valid
    if (source < 0) or (source >= len(graph.array)):
        return graph

    # check if dest valid
    if (dest >= len(graph.array)) or (dest < 0):
        return graph

    # Delete by calling delete on head of Linked List
    # Note: the delete method caters for if the edge does not exist
    graph.array[source].delete(dest)
    return graph


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 0)

g.print_graph()

remove_edge(g, 1, 3)

g.print_graph()
