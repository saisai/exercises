
from typing import List

class S:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        for i in range(n + 1):
            ranges[i] = [i - ranges[i], i + ranges[i]]
        
        ranges.sort(key = lambda x : x[0])
        ans = 1
        curr = prev = 0
        maxval = -1
        while prev < n + 1:
            while prev < n + 1 and ranges[prev][0] <= curr:
                maxval = max(maxval, ranges[prev][1])
                prev += 1
            if maxval >= n:
                return ans
            elif maxval == curr:
                return -1
            else:
                curr = maxval
                ans += 1
        return -1
    

n = 5
ranges = [3,4,1,1,0,0]
print(S().minTaps(n, ranges))