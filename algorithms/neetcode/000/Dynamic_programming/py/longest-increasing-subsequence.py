
class S:

    def __call__(self, nums):

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
class SS:
    def __call__(self, nums):
        lis = 0
        length = len(nums)       
        def dfs(i, nums):            
            if not nums:
                return
            for i in nums:                
                newnums = list(filter(lambda x: x != i, nums))
                dfs(i , newnums)
                print(i)
        dfs('', nums)
#nums = [10,9,2,5,3,7,101,18]

nums = [1,3,5]
print(SS()(nums))
