
class S:

    def __call__(self, nums):

        dp = dict()

        def maxFromHere(i):

            if i >= len(nums):
                return 0
            if i not in dp:
                dp[i] = max(maxFromHere(i+1), nums[i] + maxFromHere(i + 2))
            return dp[i]
        return maxFromHere(0)


nums = [2,7,9,3,1]

print(S()(nums))

