

from typing import List

from utils import TreeNode

class S:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(l, r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m  + 1, r)
            return root

        return helper(0, len(nums) - 1)

nums = [-10,-3,0,5,9]
result = S().sortedArrayToBST(nums)

print(result)
