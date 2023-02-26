
from typing import List

class S:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]
arr = [1,2,3,4,5]
k = 4
x = 3
print(S().findClosestElements(arr, k, x))
