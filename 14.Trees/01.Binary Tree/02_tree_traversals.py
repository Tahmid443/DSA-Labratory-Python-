class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


def inorder_iter(root):
    res, stack, curr = [], [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Inorder:", inorder(root))
    print("Preorder:", preorder(root))
    print("Postorder:", postorder(root))
    print("Inorder iter:", inorder_iter(root))
