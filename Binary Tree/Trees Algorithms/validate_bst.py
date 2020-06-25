"""Validate the Binary search tree"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def is_valid_bst(root):

    def helper(root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return True

        if root.val <= lower or root.val >= upper:
            return False
        return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

    return helper(root)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(is_valid_bst(root))
