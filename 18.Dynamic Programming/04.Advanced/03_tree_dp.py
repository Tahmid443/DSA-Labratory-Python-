class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def rob_tree(root):
    def helper(node):
        if not node:
            return (0, 0)
        l_rob, l_not = helper(node.left)
        r_rob, r_not = helper(node.right)
        rob = node.val + l_not + r_not
        not_rob = max(l_rob, l_not) + max(r_rob, r_not)
        return (rob, not_rob)

    return max(helper(root))


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(rob_tree(root))
