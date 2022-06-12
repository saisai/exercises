import pdb
def subsets(nums):
    def backtrack(res, nums, stack, pos):
        pdb.set_trace()
        if pos == len(nums):
            res.append(stack[:])
        else:
            stack.append(nums[pos])
            backtrack(res, nums, stack, pos+1)
            stack.pop()
            backtrack(res, nums, stack, pos+1)
    res = []
    backtrack(res, nums, [], 0)
    return res
print(subsets([1, 2, 3]))

#https://github.com/keon/algorithms/blob/master/algorithms/backtrack/subsets.py