
from treenode import TreeNode

class S:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

result = S().invertTree(root)

root.printLevelOrder(result)

print()
root.printPostorder(result)

print()
root.printInorder(result)

print()
root.printPreorder(result)
