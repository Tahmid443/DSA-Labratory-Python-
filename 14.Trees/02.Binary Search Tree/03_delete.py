class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Two children: find inorder successor
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete(root.right, succ.val)
    return root


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root = delete(root, 3)
    print(inorder(root))
