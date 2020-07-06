class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def nth_to_last_node(head, n):

    if not head:
        return

    left = right = head

    for _ in range(n-1):

        if not right.next:
            return

        right = right.next

    while right.next:
        left = left.next
        right = right.next

    return left.value


llist1 = Node(1)
llist2 = Node(2)
llist3 = Node(3)
llist4 = Node(4)
llist5 = Node(5)

llist1.next = llist2
llist2.next = llist3
llist3.next = llist4
llist4.next = llist5

print(nth_to_last_node(llist1, 3))
