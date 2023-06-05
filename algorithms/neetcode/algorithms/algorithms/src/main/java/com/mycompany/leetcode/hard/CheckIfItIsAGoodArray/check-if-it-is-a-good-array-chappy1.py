
from typing import List

class S:
    def isGoodArray(self, nums: List[int]) -> bool:
        from math import gcd
        from functools import reduce
        
        array_gcd = reduce(gcd, nums)
        
        return array_gcd == 1
    

nums = [12,5,7,23]
    
print(S().isGoodArray(nums))