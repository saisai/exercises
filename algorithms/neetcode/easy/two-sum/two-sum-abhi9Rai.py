'''
https://leetcode.com/problems/two-sum/
https://leetcode.com/problems/two-sum/discuss/1378197/Simple-oror-100-faster-oror-5-Lines-code-oror-Well-Explained
'''
from typing import List

class S:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = dict()

        for i in range(len(nums)):
            sec = target - nums[i]
            if sec not in store:
                store[nums[i]] = i
            else:
                return [store[sec], i]
            

nums = [2,7,11,15]
target = 9
print(S().twoSum(nums, target))
