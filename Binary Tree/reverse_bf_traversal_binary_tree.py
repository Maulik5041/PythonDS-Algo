"""Implementation of reverse breadth order traversal in a binary tree"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def __str__(self):
        s = ""
        for i, _ in enumerate(self.items):
            s += str(self.items[i].value) + " - "

        return s


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")

        if traversal_type == "inorder":
            return self.inorder_print(tree.root, "")

        if traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        if traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        if traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)

        print(f"The traversal type {(str(traversal_type))} is not supported.")
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + " - ")

        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + " - "
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)

            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + " - "

        return traversal


# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7-
# 4-2-5-6-3-7-1-
# 1-2-3-4-5-6-7-
# 4-5-6-7-2-3-1-

#             1
#            /  \
#           /    \
#          2      3
#         /  \   / \
#        4    5 6   7

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print("------------Pre-order Traversal-------------")
print(tree.print_tree("preorder"), "\n")

print("-------------In-order Traversal------------")
print(tree.print_tree("inorder"), "\n")

print("--------------Post-order Traversal-----------")
print(tree.print_tree("postorder"), "\n")

print("--------------Level-order Traversal-----------")
print(tree.print_tree("levelorder"), "\n")

print("--------------Reverse Level-order Traversal-----------")
print(tree.print_tree("reverse_levelorder"))
