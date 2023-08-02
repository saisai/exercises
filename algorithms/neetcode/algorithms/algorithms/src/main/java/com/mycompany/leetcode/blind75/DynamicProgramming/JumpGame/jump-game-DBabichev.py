
from itertools import accumulate

class S:
    def canJump(self, nums):
        t = list(accumulate([i + num for i, num in enumerate(nums)], max))
        return all(i != t[i] for i in range(len(t) - 1))

nums = [2,3,1,1,4]
print(S().canJump(nums))
