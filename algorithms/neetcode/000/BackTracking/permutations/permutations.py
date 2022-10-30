
'''

https://www.youtube.com/watch?v=s7AvT7cGdSo&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=2&ab_channel=NeetCode
https://leetcode.com/problems/permutations/

'''

from typing import List

class S:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        # base case
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

nums = [1, 2, 3]
print(S().permute(nums))
