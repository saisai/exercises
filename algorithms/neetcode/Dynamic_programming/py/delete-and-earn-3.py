
from collections import defaultdict

class S:

    def deleteAndEarn(self, nums):

        dic, prev = defaultdict(int), -1

        prevMax = leftMax = 0
        for i in nums: dic[i] += 1

        get = lambda i: i * dic.get(i, 0)

        for i in sorted(dic):
            temp = prevMax
            if i - 1 == prev: prevMax = max(prevMax, get(i) + leftMax)
            else: prevMax = get(i) + prevMax
            leftMax = temp
            prev = i
        return prevMax


nums = [2,2,3,3,3,4]

print(S().deleteAndEarn(nums))
# https://leetcode.com/problems/delete-and-earn/discuss/1821905/Python-easy-and-clean-solution-or-Explained
