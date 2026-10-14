class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


if __name__ == "__main__":
    root = None
    for v in [5, 3, 8, 1, 4, 7, 9]:
        root = insert(root, v)
    print(inorder(root))
