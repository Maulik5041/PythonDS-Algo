"""Check whether or not there is a cycle in a singly linked list"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next is not None:

        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False


list1 = Node(1)
list2 = Node(2)
list3 = Node(3)

list1.next = list2
list2.next = list3
list3.next = list1

a = Node('a')
b = Node('b')
c = Node('c')

a.next = c
c.next = b
b.next = None


def cycle_check_test():

    assert cycle_check(list1) is True
    assert cycle_check(a) is False
    print("All test cases passed")


if __name__ == '__main__':
    cycle_check_test()
