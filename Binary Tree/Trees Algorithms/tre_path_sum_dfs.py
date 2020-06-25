"""Tree path sum using Depth First search"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def has_path(root, sum_val):
    if not root:
        return False

    if root.val == sum_val and not root.left and not root.right:
        return True

    return has_path(root.left, sum_val - root.val) or has_path(root.right, sum_val - root.val)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(has_path(root, 20))
