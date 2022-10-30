'''
https://www.youtube.com/watch?v=Vn2v6ajA7U0&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=19&ab_channel=NeetCode

https://leetcode.com/problems/subsets-ii/

'''
class S:
    def subsetsWithDup(self, nums):

        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res


nums = [1,2,2]
print(S().subsetsWithDup(nums))
