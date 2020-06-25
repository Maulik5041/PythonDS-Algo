"""Zigzag traversal in a Binary tree"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def zig_zag_tree(root):
    result = deque()
    if not root:
        return result

    queue = deque()
    queue.append(root)
    level = 1

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            if level % 2 == 0:
                current_level.insert(0, current_node.val)
            else:
                current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)
        level += 1

    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)

print(zig_zag_tree(root))
