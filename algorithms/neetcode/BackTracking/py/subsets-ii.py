import pdb
class S:
    def __call__(self, nums):
        res = []
        nums.sort()
        def backtrack(i, subset):
            pdb.set_trace()
            if i == len(nums):
                res.append(subset[::])
                return
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res

print(S()([1, 2, 2]))

# https://www.youtube.com/watch?v=Vn2v6ajA7U0&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=19&ab_channel=NeetCode
# https://leetcode.com/problems/subsets-ii/

