class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class S:
    def sumNumbers(self, root):
        self.total = 0

        def dfs(n, s):
            if n:
                s = 10*s + n.val
                if not n.left and not n.right:
                    self.total += s
                else:
                    dfs(n.left, s)
                    dfs(n.right, s)
        dfs(root, 0)

        return self.total

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(S().sumNumbers(root))

# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/1060721/clean-python-high-speed-dfs

