class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def search(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    print(search(root, 3).val)
    print(search(root, 10))
