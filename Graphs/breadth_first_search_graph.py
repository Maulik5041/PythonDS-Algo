"""Implement the BFS algorithm"""


# ----> Create a Node Class with data as the arhument

# ----> Create Linked List class with the operations as:
#        getting the head node
#        checking if it is empty list
#        inserting at the head
#        inserting at the tail
#        checking the length
#        printing the list
#        deleting the head
#        deleting
#        searching in the linked list
#        removing the duplicates

# ----> Create a Queue class with the operations as:
#        check if it is empty
#        accessing the front
#        accessing the back
#        Enqueing
#        Dequeing

# ----> Create a Stack class with the operations as:
#        checking if it is empty
#        accessing the top element
#        checking the size of the stack
#        pushing the element
#        popping the element

# ----> Creating the Graph class with the operations:
#        adding the edge
#        printing the graph

# ----> Creating a Graph object


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
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        return self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()


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
            return self.head

        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        return

    def length(self):
        if self.is_empty():
            return None

        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next

        return count

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return None

        curr = self.head
        while curr.next is not None:
            print(curr.data, end=" -> ")
            curr = curr.next

        print(curr.data, " -> None")
        return True

    def delete_at_head(self):
        first_element = self.head
        if first_element is not None:
            self.head = first_element.next
            first_element.next = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():
            print("List is Empty")
            return deleted
        curr = self.head
        prev = None
        if curr.data is value:
            self.delete_at_head()
            deleted = True
            return deleted

        while curr.data is not None:
            if value is curr.data:
                prev.next = curr.next
                curr.next = None
                deleted = True
                break
            prev = curr
            curr = curr.next

        return deleted

    def search(self, data):
        if self.is_empty():
            print("List is Empty")
            return None

        curr = self.head
        while curr is not None:
            if curr.data is data:
                return curr
            curr = curr.next

        print(data, " is not in List!")
        return None

    def remove_duplicates(self):
        if self.is_empty():
            return

        if self.get_head().next is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node
            while inner_node:
                if inner_node.next:
                    if outer_node.data == inner_node.next.data:
                        new_next = inner_node.next.next
                        inner_node.next = new_next
                    else:
                        inner_node = inner_node.next
                else:
                    inner_node = inner_node.next
            outer_node = outer_node.next
        return


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
        print(">>Adjacency List of Directed Graph<<")

        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


def bfs_traversal_helper(g, source, visited):
    result = ""

    queue = Queue()
    queue.enqueue(source)
    visited[source] = True

    while (queue.is_empty()) is False:
        curr = queue.dequeue()
        result += str(curr)
        temp = g.array[curr].head
        while temp is not None:
            if visited[temp.data] is False:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next
    return result, visited


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    result, visited = bfs_traversal_helper(g, source, visited)

    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result


g = Graph(4)
num_of_vertices = g.vertices

if num_of_vertices == 0:
    print("Graph is empty")
elif num_of_vertices < 0:
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)

    print(bfs_traversal(g, 0))
