
class S:

    @classmethod
    def canPartition(cls, nums):

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            print(i)
            nextDP = set()
            for t in dp:
                #if (t + nums[i]) == target:
                #    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        print(dp)

        return True if target in dp else False



nums = [1,5,11,5]
print(S.canPartition(nums))

