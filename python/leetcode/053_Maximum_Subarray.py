"""
# https://leetcode.com/problems/maximum-subarray/
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For each num calculate the max subarray sum ending with that num as either num alone (if previous sum was -ve) or
# num + previous sum (if previous sum was +ve)
# Time - O(n)
# Space - O(1)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall_max = float('-inf')
        max_ending_here = 0


        for num in nums:
            if max_ending_here > 0:
                max_ending_here += num
            else:
                max_ending_here = num
            overall_max = max(overall_max, max_ending_here)

        return overall_max


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
