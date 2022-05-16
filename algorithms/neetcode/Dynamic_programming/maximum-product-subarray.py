
class S:
    def __call__(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
nums = [2,3,-2,4]
print(S()(nums))

