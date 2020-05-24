"""Finding the shortest path between 2 vertices in a directed graph"""


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
        print
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


def find_min(g, a, b):
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes
    # Make a node visited whenever we enqueue it into queue
    visited = [False] * num_of_vertices

    # For keeping a track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Bredth First Traversal and enqueue source in it
    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True

    while not queue.is_empty():

        # Dequeue a vertex/node from the queue and add it to result
        current_node = queue.dequeue()

        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while temp:
            if (not visited[temp.data]) or (temp.data is b):
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element

    return -1


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
print(find_min(g, 1, 5))
