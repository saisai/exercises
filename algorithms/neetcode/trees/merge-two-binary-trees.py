

from treenode import TreeNode

class S:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1 and not t2:
            return None

        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        root = TreeNode(v1 + v2)

        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t2 else None, t2.right if t2 else None)

        return root

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

print("t1 ", t1)
print("t2", t2)
result = S().mergeTrees(t1, t2)

print(result)

