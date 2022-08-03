'''
https://www.youtube.com/watch?v=jzZsG8n2R9A&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=9&ab_channel=NeetCode
https://leetcode.com/problems/3sum/
'''


from typing import List

class S:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


nums = [-1,0,1,2,-1,-4]
print(S().threeSum(nums))
