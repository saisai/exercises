
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class S:

    def convertBST(self, root):
        curSum = 0

        def dfs(node):
            if not node:
                return

            nonlocal curSum
            dfs(node.right)
            tmp = node.val
            node.val += curSum
            curSum += tmp
            dfs(node.left)
        dfs(root)
        return root


root = TreeNode(30)
root.left = TreeNode(36)
root.right = TreeNode(21)
root.left.left = TreeNode(36)
root.left.right = TreeNode(35)
root.left.right.right = TreeNode(33)

root.right.left = TreeNode(26)
root.right.right = TreeNode(15)
root.right.right.right = TreeNode(8)


result = S().convertBST(root)

def preorder(root):

    if root is None:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):

    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

preorder(root)
print('')
postorder(root)
print('')
inorder(root)





