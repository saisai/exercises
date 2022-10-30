

def preorder(root):

    if root is None:
        return

    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)

