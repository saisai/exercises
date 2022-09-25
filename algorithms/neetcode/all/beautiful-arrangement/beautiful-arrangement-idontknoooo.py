
class S:
    def countArrangment(self, N: int) -> int:
        def dfs(index, nums):
            nonlocal ans, n
            if index ==n: ans += 1; return
            for i in range(index, n):
                if not nums[i] % (index+1) or not (index+1) % nums[1]:
                    nums[i], nums[index] = nums[index], nums[i]
                    dfs(index+1, nums)
                    nums[i], nums[index] = nums[index], nums[i]
        nums = [i for i in range(1, N+1)]
        ans, n = 0, len(nums)
        dfs(0, nums)
        return ans
N = 2
print(S().countArrangment(N))
