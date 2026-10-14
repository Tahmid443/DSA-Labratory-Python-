class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(root.val, root.left.val, root.right.val)
