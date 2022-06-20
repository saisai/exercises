
"""
The longest array takes the form of [2,4,6,...,2x-2,2x+leftover] and 0 <= leftover < 2x+2.
A quick prove is we cannot make this array longer.
We cannot split any existing element as the smallest of resulting elements is smaller than 2x and must collide with one of the elements as the array contains all the even integers that is smaller than 2x.
Another choise is to add one of the elements ai to 2x+leftover and then split it into 3 integers, which is not possible either as ai+2x+leftover < 2x-2+2x+2x+2 < 6x. We cannot split into 3 unique integers that are all larger than 2x-2.

Then we just use math to find out that x in O(1) time. As [2,4,6,...,2x-2,2x] is an arithmetic sequence whose sum is x(x+1). finalSum >= x(x+1) or x^2+x-finalSum <= 0, with quadratic formula, gives us x <= (sqrt(4finalSum+1)-1)/2. We want to get the largest x so x = int(((4*finalSum+1)**0.5-1)/2). Then we just add the leftover to the last element 2x.

https://leetcode.com/problems/maximum-split-of-positive-even-integers/discuss/1785403/python-greedy-math-o1-time
https://leetcode.com/problems/maximum-split-of-positive-even-integers/


"""
from typing import List

class Solution:
    def maximumEvenSplit(self, s: int) -> List[int]:
        if s & 1:
            return []
        x = int(((4*s+1)**0.5-1)/2)
        leftover = s-x*(x+1)
        return list(range(2, 2*x,2)) + [2*x+leftover]

finalSum = 12
print(Solution().maximumEvenSplit(finalSum))


