"""Implement Singly Linked List"""


import random


# Linked List Node Class
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Only for doubly linked list
        self.arbitrary = None


# Linked List class
def insert_at_head(head, data):

    new_node = LinkedListNode(data)
    new_node.next = head

    return new_node


def insert_at_tail(head, node):

    if not head:
        return node

    temp = head

    while temp.next:
        temp = temp.next

    temp.next = node
    return head


def create_random_list(length):

    list_head = None
    for i in range(0, length):
        list_head = insert_at_head(list_head, random.randrange(1, 100))

    return list_head


def create_linked_list(lst):

    list_head = None
    for x in reversed(lst):
        list_head = insert_at_head(list_head, x)

    return list_head


def display(head):

    temp = head
    while temp:
        print(str(temp.data), end='')
        temp = temp.next

        if temp:
            print(", ", end='')
    print()
    return


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second
