from collections import deque


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):

        if traversal_type == "preorder":
            return self.preorder_print(tree1.root, "")

        if traversal_type == "inorder":
            return self.inorder_print(tree1.root, "")

        if traversal_type == "postorder":
            return self.postorder_print(tree1.root, "")

        print(f"Traversal type {traversal_type} is not supported.")
        return False

    def preorder_print(self, start, traversal):

        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):

        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + "-"

        return traversal


tree1 = BinaryTree(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)
tree1.root.right.left = Node(6)
tree1.root.right.right = Node(7)

print(tree1.print_tree("preorder"), "\n\n\n")
print(tree1.print_tree("inorder"), "\n\n\n")
print(tree1.print_tree("postorder"))


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node2:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree2:

    def __init__(self, root):
        self.root = Node2(root)

    def print_tree(self, traversal_type):

        if traversal_type == "preorder":
            return self.preorder_print(tree2.root, "")

        if traversal_type == "inorder":
            return self.inorder_print(tree2.root, "")

        if traversal_type == "postorder":
            return self.postorder_print(tree2.root, "")

        if traversal_type == "levelorder":
            return self.levelorder_print(tree2.root)

    def levelorder_print(self, start):

        if not start:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:

            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def preorder_print(self, start, traversal):

        if not start:
            return

        traversal += str(start.value) + "-"
        traversal = self.preorder_print(start.left, traversal)
        traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):

        if not start:
            return

        traversal = self.preorder_print(start.left, traversal)
        traversal += str(start.value) + "-"
        traversal = self.preorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):

        if not start:
            return

        traversal = self.preorder_print(start.left, traversal)
        traversal = self.preorder_print(start.right, traversal)
        traversal += str(start.value) + "-"

        return traversal


tree2 = BinaryTree2(10)
tree2.root.left = Node2(11)
tree2.root.right = Node2(12)
tree2.root.left.left = Node2(14)
tree2.root.left.right = Node2(15)
tree2.root.right.left = Node2(17)
tree2.root.right.right = Node2(18)
tree2.root.left.right.left = Node2(19)

print(tree2.print_tree("levelorder"))
