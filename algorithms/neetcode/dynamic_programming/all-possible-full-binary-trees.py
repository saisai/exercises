
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class S:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        # ret the list of fbt with n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]

            res = []
            for l in range(n):
                r = n - 1 - 1
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            return res

        return backtrack(n)
n = 7
result = S().allPossibleFBT(n)




