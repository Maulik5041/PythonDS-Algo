"""Check if the given binary tree is symmetric or not"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def is_symmetric(root):
    if not root:
        return True
    return dfs(root.left, root.right)


def dfs(l, r):
    if l and r:
        return (l.val == r.val) and dfs(l.left, r.right) and dfs(l.right, r.left)
    return l == r


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(is_symmetric(root))
