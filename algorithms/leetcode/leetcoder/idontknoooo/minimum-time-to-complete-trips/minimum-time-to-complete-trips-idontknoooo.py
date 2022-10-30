'''
Explanation
Typical binary search problem
Check if we can finished enough trips within time mid. This is linear.
Then use binary search to find the shortest time
Initial upper end value should be int(1e14), due to the constraint


https://leetcode.com/problems/minimum-time-to-complete-trips/discuss/1802959/python-3-binary-search-explanation
https://leetcode.com/problems/minimum-time-to-complete-trips/
'''
from typing import List

class S:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l ,r = 1, int(1e14)
        
        def ok(mid):
            #nonlocal time
            #print(time)            
            cnt = 0
            for t in time:
                cnt += mid // t
            return cnt >= totalTrips

        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

time = [1,2,3]
totalTrips = 5
print(S().minimumTime(time, totalTrips))

