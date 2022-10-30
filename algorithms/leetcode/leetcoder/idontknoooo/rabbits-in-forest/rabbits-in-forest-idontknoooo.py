'''
https://leetcode.com/problems/rabbits-in-forest/
https://leetcode.com/problems/rabbits-in-forest/solutions/838445/python-3-hash-table-1-liner-explanations/

Explanation
    Count frequency of each number
    If num+1 <= frequency meaning there are num+1 for some color
    If num+1 > frequency meaning there are more than num+1 for some color
        Count how many num+1 are there, take the ceil
        Add (key+1) * math.ceil(freq / (key+1)) to ans
Implementation
'''
import math
import collections
from typing import List


class S:

    def numRabbits(self, answers: List[int]) -> int:
        return sum((key + 1) * math.ceil(freq / (key + 1)) if key + 1 < freq else key + 1 for key, freq in collections.Counter(answers).items())

answers = [1,1,2]
print(S().numRabbits(answers))


class SS:
    def numRabbits(self, answers: List[int]) -> int:
        ans, cnt = 0, collections.Counter(answers)
        print(cnt)
        print(cnt.items())
        for key, freq in cnt.items():
            if key + 1 < freq: ans += (key+1) * math.ceil(freq / (key+1))
            else: ans += key + 1
        return ans

print(SS().numRabbits(answers))

