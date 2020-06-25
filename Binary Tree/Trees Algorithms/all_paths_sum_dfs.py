class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_paths(root, sum_val):
    all_paths = []
    find_paths_recursive(root, sum_val, [], all_paths)
    return all_paths


def find_paths_recursive(root, sum_val, current_path, all_paths):
    if not root:
        return

    current_path.append(root.val)

    if root.val == sum_val and not root.left and not root.right:
        all_paths.append(list(current_path))
    else:
        find_paths_recursive(root.left, sum_val - root.val, current_path, all_paths)
        find_paths_recursive(root.right, sum_val - root.val, current_path, all_paths)

    del current_path[-1]


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(find_paths(root, 23))
