"""Implementation of Directed Graph bsaed on Adjacency list model"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
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
            return self.head

        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)

        if not self.get_head():
            self.head = new_node
            return

        curr = self.get_head()
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        return

    def length(self):
        curr = self.get_head()
        length = 0

        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        curr = self.head
        while curr.next is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(curr.data, "-> None")
        return True


class Graph:
    """
    self.vertices = Total number of vertices
    self.array = Defining a list which can hold
                 multiple LinkedLists equal to the
                 number of vertices in the graph
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        # Creating a new LinkedList for each vertex of the list
        for i in range(vertices):
            new_ll = LinkedList()
            self.array.append(new_ll)

    # Function to add an edge from source --> destination
    def add_edge(self, source, destination):
        if (source < self.vertices) and (destination < self.vertices):
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph
            # self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")

        for i in range(self.vertices):
            print("|", i, end=" | => ")
            curr = self.array[i].get_head()
            while curr is not None:
                print("[", curr.data, end=" ] -> ")
                curr = curr.next
            print("None")


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

print(g.array[1].get_head().data)
