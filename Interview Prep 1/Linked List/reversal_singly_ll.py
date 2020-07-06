"""Reverse a singly linked list"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def reverse_list(self):

        curr_node = self.head
        prev_node = None

        while curr_node:

            temp = curr_node.next
            curr_node.next = prev_node
            prev_node.next = curr_node
            curr_node = temp

        self.head = prev_node

    def insert_at_head(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        return new_node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next


rev_list = LinkedList()
rev_list.insert_at_head(2)
rev_list.insert_at_head(3)
rev_list.insert_at_head(4)
rev_list.insert_at_head(5)

rev_list.print_list()

rev_list.reverse_list()

rev_list.print_list()
