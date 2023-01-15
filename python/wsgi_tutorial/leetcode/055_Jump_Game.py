"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
https://leetcode.com/problems/jump-game/


_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/jump-game/
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Record the maximum index that can be reached. Initially this is index 0.
# Iterate through nums, returning False an index cannot be reached.
# Else update the maximum index with the current index + its value (the maximum jump).
# Time - O(n)
# Space - O(1)

"""

class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        """
        max_index = 0

        for i, num in enumerate(nums):
            if i > max_index:
                return False
            max_index = max(max_index, i + num)
            print(nums, i, max_index, num)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))