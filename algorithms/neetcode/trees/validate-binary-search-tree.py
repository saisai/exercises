
from utils import TreeNode

class S:
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False;

            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = S().isValidBST(root)
print(result)
