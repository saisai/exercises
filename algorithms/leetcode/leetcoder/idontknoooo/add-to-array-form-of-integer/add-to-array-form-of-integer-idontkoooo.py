
from typing import List

class S:

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:

        carry = 0
        for i in range(len(A) -1, -1, -1):  # Reverse adding numbers, K or carry might left over
            tmp = A[i] + K % 10 + carry
            K //= 10
            if tmp > 9:                     # If greater than 9, carry and only add one digit
                carry = 1
                A[i] = tmp % 10
            else:                           # If less than 9, don't carry and add tmp
                carry = 0
                A[i] = tmp

        if K or carry:                     # If K or carry
            K += carry
            arr = []                        # Adding numbers to arr (from right to left)
            while K:
                arr.append(K%10)
                K //= 10
            arr = arr[::-1]                 # Reverse the arr
            # or use map
            # arr = list(map(int, str(K)))
            return arr + A                  # Append A to the end of arr
        return A

num = [1,2,0,0]
k = 34
print(S().addToArrayForm(num, k))

