
from typing import List

class S:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:

        list_to_int = int("".join(map(str, A)))
        result = list_to_int + K
        int_to_list = list(map(int, str(result)))
        return int_to_list


for A, K in [([1, 2, 0, 0], 34),
        ([2,7,4], 181),
        ([2, 1, 5], 806)]:
    print(S().addToArrayForm(A, K))

