
class S:

    def removeDuplicates(self, nums):

        l = 1
        test = [nums[0]]

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                test.append(nums[r])
                l += 1
        print(test)
        print(nums)
        return l

nums = [0,0,1,1,1,2,2,3,3,4]
print(S().removeDuplicates(nums))

