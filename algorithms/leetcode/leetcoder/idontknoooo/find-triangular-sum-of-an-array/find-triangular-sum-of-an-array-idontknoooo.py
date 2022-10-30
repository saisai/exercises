
'''
https://leetcode.com/problems/find-triangular-sum-of-an-array/discuss/1907687/python-3-in-place-compression-explanation
https://leetcode.com/problems/find-triangular-sum-of-an-array/

Explanation
The below solution using the same idea as in-place compress in question 443. String Compression
Adding pairs from the right side of the array, and move the ending index to left
    For example -[1,2,3,4,5], n=5
    1st iteration : [3,5,7,9 | 5], n=4
    2nd iteration: [8,2,6 | 9,5], n=3
    3rd iteration : [0,8 | 6,9,5], n=2
    4th iteration : [8 | 8,6,9,5], n=1
Stop when ending index equals to 1
Implenetation

'''

from typing import List

class S:

    @classmethod
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            prev = nums[n-1]
            for right in range(n-1, 0, -1):
                prev, nums[right-1] = nums[right-1], (prev + nums[right-1]) % 10
            n -= 1
        return nums[0]


nums = [1, 2, 3, 4, 5]
print(S.triangularSum(nums))
