class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):

        if not self.left:
            self.left = BinaryTree(new_node)

        else:
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):

        if not self.right:
            self.right = BinaryTree(new_node)

        else:
            temp = BinaryTree(new_node)
            temp.right = self.right
            self.right = temp

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root(self, val):
        self.key = val

    def get_root(self):
        return self.key


r = BinaryTree('a')

print(r.get_root())
print(r.get_left())

r.insert_left('b')
print(r.get_left().get_root())

r.insert_right('c')
print(r.get_right().get_root())
