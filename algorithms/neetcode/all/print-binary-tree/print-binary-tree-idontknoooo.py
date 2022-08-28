'''
https://leetcode.com/problems/print-binary-tree/discuss/1384379/python-3-dfs-bfs-level-order-traversal-explanation
https://leetcode.com/problems/print-binary-tree/discuss/1384379/python-3-dfs-bfs-level-order-traversal-explanation
https://leetcode.com/problems/print-binary-tree/
'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class S:

    def printTree(self, root: TreeNode) -> List[List[str]]:

        height = 0

        def dfs(node, h):
            nonlocal height
            height = max(height, h)
            if node.left:
                dfs(node.left, h+1)
            if node.right:
                dfs(node.right, h+1)
        dfs(root, 0)
        n = 2 ** (height + 1) - 1
        offset = (n - 1) // 2
        ans = [[''] * n for _ in range(height + 1)]
        q = [(root, 0, offset)]
        for i in range(height+1):
            tmp_q = []
            while q:
                cur, r, c = q.pop()
                ans[r][c] = str(cur.val)
                if cur.left:
                    tmp_q.append((cur.left, r+1, c-2 ** (height - r - 1)))
                if cur.right:
                    tmp_q.append((cur.right, r + 1, c+2 ** (height - r - 1)))
            q = tmp_q
        return ans

root = TreeNode(1)
root.left = TreeNode(2)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print(S().printTree(root))

