
from typing import List

class S:
    def findNumbers(self, nums: List[int]) -> int:
        even_num_of_digits = 0
        
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_num_of_digits += 1
        return even_num_of_digits

nums = [12,345,2,6,7896]
print(S().findNumbers(nums))