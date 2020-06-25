"""Check if two binary trees are identical. Use DFS"""


def are_identical(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and root2:
        return root1.data == root2.data and are_identical(root1.left, root1.left) and are_identical(root1.right, root2.right)
