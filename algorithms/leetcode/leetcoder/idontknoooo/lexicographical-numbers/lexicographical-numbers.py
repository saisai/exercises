'''
https://leetcode.com/problems/lexicographical-numbers/
https://leetcode.com/problems/lexicographical-numbers/solutions/810448/python-3-one-liner-cheat-sort-string/

'''
from typing import List

class S:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(i) for i in sorted([str(i) for i in range(1, n+1)])]

for n in [13 , 2]:
    print(S().lexicalOrder(n))
