
'''
https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/discuss/1846786/python3-scan-the-array

'''
from typing import List

class S:
    def maximumTop(self, nums: List[int], k: int) -> int:

        if len(nums) == 1 and k & 1: return -1
        ans = 0
        for i in range(min(k-1, len(nums))): ans = max(ans, nums[i])
        if k < len(nums): ans = max(ans, nums[k])
        return ans
nums = [5,2,2,4,0,6]
k = 4
print(S().maximumTop(nums, k))
