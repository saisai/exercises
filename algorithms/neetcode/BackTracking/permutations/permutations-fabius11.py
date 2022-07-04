
'''

https://leetcode.com/problems/permutations/discuss/541908/Python-BFS-solution
https://leetcode.com/problems/permutations/

'''
from collections import deque
from typing import List

class S:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        ans = []
        queue = deque([([], nums)])

        while queue:
            arr, options = queue.popleft()

            for i in range(len(options)):
                next_options = options[:i] + options[i+1:]
                new_arr= arr + [options[i]]

                if next_options:
                    queue.append((new_arr, next_options))
                else:
                    ans.append(new_arr)
        return ans

nums = [1, 2, 3]
print(S().permute(nums))
