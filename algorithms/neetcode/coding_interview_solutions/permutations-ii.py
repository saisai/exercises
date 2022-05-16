class S:
    def __call__(self, nums):
        res = []
        perm = []
        count = { n:0 for n in nums }
        for n in nums:
            count[n]  += 1
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()
        dfs()
        return res
nums = [1, 2, 1]
print(S()(nums))
