'''
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/2516754/python-3-brutal-force-10-lines-explanation
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

Explanation
    Get all subarrays and store to ans
    Sort ans
    Sum them up
    mod int(1e9+7)
Implementation
'''

from typing import List

class S:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        ans = [nums[0]]
        print(ans)
        for i in range(1, n):    
            ans.append(nums[i])
            nums[i] += nums[i-1]            
            ans.append(nums[i])
            for j in range(i-1): ans.append(nums[i] - nums[j])            
        ans.sort()
        print(ans)
        print(ans[left-1:right])
        return sum(ans[left-1:right]) % 1000000007

nums = [1,2,3,4]
n = 4
left = 1
right = 5
print(S().rangeSum(nums, n, left, right))
