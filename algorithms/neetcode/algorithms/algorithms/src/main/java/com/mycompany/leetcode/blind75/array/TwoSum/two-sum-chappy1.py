from typing import List

class S:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        i = 0
        while target - nums[i] not in checked:
            checked[nums[i]] = i
            i += 1
        
        return [checked[target-nums[i]], i]

nums = [2,7,11,15]
target = 9
print(S().twoSum(nums, target))

# https://leetcode.com/problems/two-sum/solutions/3140107/solution/