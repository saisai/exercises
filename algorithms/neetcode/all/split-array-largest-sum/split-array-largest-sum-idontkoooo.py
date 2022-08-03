'''
https://leetcode.com/problems/split-array-largest-sum/
https://leetcode.com/problems/split-array-largest-sum/discuss/1899661/python-3-binary-search-explanation
'''

from typing import List

class S:

    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = min(nums), sum(nums)
        def ok(mx):
            nonlocal m
            cur = cnt = 0
            for num in nums:
                if num > mx:
                    return False
                elif cur + num <= mx:
                    cur += num
                else:
                    cur, cnt = num, cnt + 1
            return cnt + 1 <= m

        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

nums = [7,2,5,10,8]
m = 2
print(S().splitArray(nums, m))
