
class S:
    def missingNumber(self, nums):
        
        result = 0
        for num in range(len(nums) + 1):
            result ^= num

        for num in nums:
            result ^= num


        return result

nums = [3,0,1]
print(S().missingNumber(nums))
