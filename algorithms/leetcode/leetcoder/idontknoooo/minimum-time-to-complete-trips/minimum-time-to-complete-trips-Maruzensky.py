'''

Idea, estimate a lower bound, and then refine.

Step 1:
How do we estimate the time needed?

For each truck t in time, we know that in every minute, 1/t trip is completed.

Therefore, sum(1/t) trips are completed per minute.

As a rough estimate, we will need T = totalTrips/sum(1/t) minutes to finish totalTrips.

Step 2:
The estimate in step 1 is only a lower bound. The reason is, we need complete trips.

Therefore, assuming that partial trips are count, we will complete totalTrips trips in T minute.

However, we need to round down evey trip, so there are only
sum( floor(T/t) ) trips completed.

After taking floor, for each truck, at most 1 trip is discarded, so the N trucks will waste at most N trips.

Step 3:
Find a systematic way to fill up the underestimated totalTrips - sum( floor(T/t) ) <= N trips.

I will do this by heap.

At time est, For each truck t, we will compute the next time for t to finish its next trip (implemented in the function ceiling(est, t) below).

Then, we push the tuple (ceiling(est, t), t) to the heap.

Then, for each pop in the heap, we know there is another trip completed, so we increment the trip count by 1 and push the next trip completion time to the heap.

Complexity analysis:
Every thing up to step 2 is O(N).

From the analysis in step 2, we know that in the worst case we need to emulate N trips.

Constructing the heap is O(N log N)

Poping and pushing in the loop is O(log N). Multiply by N, the worst case, the loop takes at most O(N log N).

So the overall algorithm is O(N log N).

2076 ms, beats 90%.

https://leetcode.com/problems/minimum-time-to-complete-trips/
https://leetcode.com/problems/minimum-time-to-complete-trips/discuss/1802899/Python-Heap-no-binary-search-O(n-log-n)
'''
from typing import List
from heapq import *

class S:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Return the smallest multiple of b strictly greather than a.
        def ceiling(a, b):
            return a // b * b + b

        # Step 1: Find est, an initial lower bound
        speed = sum(1/t for t in time)
        est = int(totalTrips/speed)

        # Step 2: Construct the heap
        trips = 0
        hp = []
        for t in time:
            # ceiling(est, t) is the next returning time for the truck t
            heappush(hp, (ceiling(est, t), t))
            # Compute trips, the number of trips actually finished at time est
            trips += est // t

        # Step 3: Heap update
        answer = est
        while trips < totalTrips:
            # Update the returing tiem as answer for every incoming trip
            answer, t = heappop(hp)
            # Push back the next returning tiem for the same truck which just returned.
            heappush(hp, (ceiling(answer, t), t))
            trips += 1
        return answer

time = [1,2,3]
totalTrips = 5
print(S().minimumTime(time, totalTrips))

