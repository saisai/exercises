
'''

https://leetcode.com/problems/permutations/

'''
from collections import deque
from typing import List

class S:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(nums, new_nums):
            if not nums:
                res.append(new_nums.copy())
                return
            for num in nums:
                lst_match = list(filter(lambda x: x != num, nums))
                new_nums.append(num)
                dfs(lst_match, new_nums)
                new_nums.pop()
                
        dfs(nums, [])
        return res

nums = [1, 2, 3]
print(S().permute(nums))
