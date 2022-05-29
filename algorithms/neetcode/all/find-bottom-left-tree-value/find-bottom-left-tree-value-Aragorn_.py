
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class S:
    def findBottomLeftValue(self, root):

        def write(val, d, x):
            self.val = val
            self.d = d
            self.x = x

        def dfs(n, d, x):
            if n:
                if d >= self.d:
                    if d > self.d or x < self.x:
                        write(n.val, d, x)

                dfs(n.left, d+1, 2*x-1)
                dfs(n.right, d+1, 2*x+1)
        write(None, -1, 0) # Initialization
        dfs(root, 0, 0)
        return self.val

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(S().findBottomLeftValue(root))

