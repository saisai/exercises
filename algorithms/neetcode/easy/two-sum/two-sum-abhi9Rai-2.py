'''
https://leetcode.com/problems/two-sum/
https://leetcode.com/problems/two-sum/discuss/1378197/Simple-oror-100-faster-oror-5-Lines-code-oror-Well-Explained

'''
from typing import List

class S:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tmp = sorted(nums)
        n, i, j = len(nums), 0, (len(nums)-1)
        while True:
            s = tmp[i] + tmp[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                break
        return [nums.index(tmp[i]), n - (nums[::-1].index(tmp[j])) - 1]

            

nums = [2,7,11,15]
target = 9
print(S().twoSum(nums, target))
