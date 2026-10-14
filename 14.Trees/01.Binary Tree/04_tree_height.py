class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(height(root))
