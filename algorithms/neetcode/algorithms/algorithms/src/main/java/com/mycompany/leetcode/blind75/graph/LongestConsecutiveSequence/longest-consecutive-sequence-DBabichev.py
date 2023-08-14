
class S:
    def longestConsecutive(self, nums):
        set_nums, ans = set(nums), 0
        for num in nums:
            if num - 1 in set_nums: continue

            nxt = num
            while nxt + 1 in set_nums:
                nxt += 1
            ans = max(ans, nxt - num + 1)

        return ans

nums = [100,4,200,1,3,2]
print(S().longestConsecutive(nums))
