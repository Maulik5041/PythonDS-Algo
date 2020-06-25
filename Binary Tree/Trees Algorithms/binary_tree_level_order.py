from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if not root:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)

    return result


root = TreeNode(12)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(9)
root.right.left = TreeNode(67)
root.right.right = TreeNode(32)

print(traverse(root))
