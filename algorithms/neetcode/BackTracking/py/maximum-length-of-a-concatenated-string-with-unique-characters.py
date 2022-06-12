
from collections import Counter

class S:
    
    @staticmethod
    def maxLength(arr):

        charSet = set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)


            return max(res, backtrack(i + 1)) # dont concatenate arr[i]

        return backtrack(0)

print(S().maxLength(arr = ["un","iq","ue"]))
#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
#https://www.youtube.com/watch?v=d4SPuvkaeoo&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=14&ab_channel=NeetCode
