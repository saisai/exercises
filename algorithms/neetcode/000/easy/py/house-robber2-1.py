
class S:

    def rob(self, nums, memo=None):

        if memo is None:
            memo = {}

        # build a string key for memo dictionary
        key = ",".join([str(x) for x in nums])
        if key in memo:
            return memo[key]


        # base cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # recursive case
        memo[key] = max(nums[0] + self.rob(nums[2:], memo), self.rob(nums[1:], memo))
        return memo[key]


nums = [2,7,9,3,1]
print(S().rob(nums))
