
class S:

    def findDifferentBinaryString(self, nums):

        n, nums = len(nums[0]), set(nums)

        def bt(s: str):
            if len(s) == n:
                if s not in nums:
                    yield s
            else:
                for c in ("0", "1"):
                    yield from bt(s + c)

        return next(bt(""))

nums = ["111","011","001"]
print(S().findDifferentBinaryString(nums))

# https://leetcode.com/problems/find-unique-binary-string/discuss/1614898/~9-line-Backtracking-in-Python-3
