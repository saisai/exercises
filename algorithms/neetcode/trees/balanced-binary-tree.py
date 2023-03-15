
from typing import Optional

import utils

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class S:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

array = [1,2,2,3,3,None,None,4,4]

root = utils.Utils().list2tree(array)

print(root)

print(S().isBalanced(root))
