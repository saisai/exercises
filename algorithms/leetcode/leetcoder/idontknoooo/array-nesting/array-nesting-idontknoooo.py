'''
https://leetcode.com/problems/array-nesting/
https://leetcode.com/problems/array-nesting/discuss/1424880/python-3-array-clean-on-explanation
Explanation
    First, you need to understand all numbers in nums are unique
    Given that, you can basically travel to the next number until you hit a cycle
    Record the length during the run
    Set visited value to -1 to avoid revisit
Implementation
'''

from typing import List

class S:

    def arrayNesting(self, nums: List[int]) -> int:
        ans = cnt = 0
        for i, idx in enumerate(nums):
            if idx < 0: continue    # avoid revisit
            while nums[idx] >= 0:
                cnt, nums[idx], idx = cnt+1, -1, nums[idx] # increment length; mark as visited; visit next value
            else:
                ans, cnt = max(ans, cnt), 0 # record length and reset `cnt`
        return ans

nums = [5,4,0,3,1,6,2]
print(S().arrayNesting(nums))
