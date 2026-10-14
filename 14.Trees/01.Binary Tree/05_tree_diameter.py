class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def diameter(root):
    best = 0

    def helper(node):
        nonlocal best
        if not node:
            return 0
        l = helper(node.left)
        r = helper(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    helper(root)
    return best


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(diameter(root))
