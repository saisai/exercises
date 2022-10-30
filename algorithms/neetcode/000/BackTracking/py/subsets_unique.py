
import pdb


def subsets_unique(nums):

    def backtrack(res, nums, stack, pos):
        #pdb.set_trace()
        if pos == len(nums):
            res.add(tuple(stack))
            #res.append(stack[:])
        else:
            # take
            stack.append(nums[pos])
            backtrack(res, nums, stack, pos+1)
            stack.pop()

            # don't take
            backtrack(res, nums,stack, pos+1)


    res = set()
    backtrack(res, nums, [], 0)
    return list(res)

print(subsets_unique([1, 2, 2]))

