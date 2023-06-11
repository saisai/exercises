
from typing import List

class S:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]

n = 2
print(S().getNoZeroIntegers(n))