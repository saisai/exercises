import pdb
def permute(nums, arr, ans):
    #pdb.set_trace()
    if not nums:
        ans.extend([arr[:]])
        #ans.extend([arr.copy()])

    for i in nums:
        newNums = list(filter(lambda x: x != i, nums))
        arr.append(i)
        permute(newNums, arr, ans)
        arr.pop()

    return ans

print(permute([1, 2, 3], [], []))

