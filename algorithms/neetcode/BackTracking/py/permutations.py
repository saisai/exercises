
def permute(nums):
    
    #print('nums ', len(nums))
    #print('arr ', len(arr))
    def per(nums, arr, ans):
        if not nums:
            if len(arr) == 3:
                print('arr ', arr)
                ans.extend(arr)
            return

        for i in nums:
            newNums = list(filter(lambda x: x != i, nums))
            arr.append(i)
            per(newNums, arr, ans)
            arr.pop()

    ans = []
    if not nums:
        return ans
    per(nums, [], ans)
    return ans

    


print(permute([4, 2, 3]))

