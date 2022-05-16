

class S:
    def __call__(self, nums):
        res = []     
        
        def backtrack(nums, mnums):        
            if not nums:
                res.append(mnums.copy())
                return
            for idx in nums:
                newnums = list(filter(lambda x: x != idx, nums))
                mnums.append(idx)
                backtrack(newnums, mnums)
                mnums.pop()
        backtrack(nums, [])
        
        return res
print(S()([1, 2, 3]))
