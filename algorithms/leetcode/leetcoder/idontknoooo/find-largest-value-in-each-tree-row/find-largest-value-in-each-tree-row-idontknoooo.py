'''
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
https://leetcode.com/problems/find-largest-value-in-each-tree-row/solutions/773511/python-3-dfs/

'''
import sys
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class S:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        d = collections.defaultdict(lambda : -sys.maxsize)
        def dfs(node, level):
            if not node: return
            if node.val > d[level]:
                d[level] = node.val
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        dfs(root, 0)
        return d.values()

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(9)

print(S().largestValues(root))
