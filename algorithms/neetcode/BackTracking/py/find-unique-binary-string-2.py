
class S:

    def findDifferentBinaryString(self, nums):

        nums = set(nums)

        def recur(string, depth):

            if depth == 0: return string if string not in nums else ""

            for value in "01":
                ans = recur(string + value, depth - 1)
                if ans: return ans
        return recur("", len(nums))

nums = ["111","011","001"]
print(S().findDifferentBinaryString(nums))

# https://leetcode.com/problems/find-unique-binary-string/discuss/1421750/Simple-python-recursive-approach-100-faster
