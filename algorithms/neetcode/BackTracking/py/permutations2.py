import pdb
def permute(nums, arr=[], ans=[]):
    if not nums:
        ans.extend([arr[:]])
        #ans.extend([arr.copy()])
        return
    for i in nums:
        print(i, nums)
        newNums = list(filter(lambda x: x != i, nums))
        arr.append(i)
        permute(newNums, arr, ans)
        arr.pop()
    return ans
print(permute([1, 2, 3]))

