from typing import List

class S:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (1 + target)
        for num in nums:
            if num <= target:
                dp[num] = 1
        for i in range(target + 1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i - num]
        return dp[-1]

nums = [1,2,3]
target = 4
print(S().combinationSum4(nums, target))
