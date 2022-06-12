
class S:

    def findDifferentBinaryString(self, nums):

        strSet = { s for s in nums }

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strSet else res

            res = backtrack(i + 1, cur)
            if res: return res

            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res: return res

        return  backtrack(0, ["0" for s in nums])

nums = ["111","011", "001"]
print(S().findDifferentBinaryString(nums))
