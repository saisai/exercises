'''
https://leetcode.com/problems/split-array-into-fibonacci-sequence/discuss/1486859/python-3-simulation-explanation
https://leetcode.com/problems/split-array-into-fibonacci-sequence/

Explanation
    Similar to 306. Additive Number
    First two numbers decide the rest sequences. Try out all combination of first two value.
    At the same time, make sure values are less than 2^31 and no leading zero numbers.
Implementation

'''

from typing import List

class S:

    def splitIntoFibonacci(self, num: str) -> List[int]:
        two_31 = 2 ** 31
        n = len(num)
        def fibo(a, b, j):
            nonlocal n
            cur = []
            while j < n:
                a, b = b, a + b
                if b > two_31: return []
                b_str = str(b)
                if num[j:].startswith(b_str):
                    cur.append(b)
                    j +=  len(b_str)
                else:
                    return []
            else:
                return cur

        for i in range(1, n):
            if i > 1 and num[0] == '0': break
            a_str = num[:i]
            a = int(num[:i])
            if a > two_31: break
            for j in range(i+1, n):
                if j > i + 1 and num[i] == '0': break
                b_str = num[i:j]
                b = int(num[i:j])
                if b > two_31: break
                cur = fibo(a, b, j)
                if not cur: continue
                return [a, b] + cur
        return []

for num in ["1101111", "112358130", "0123"]:
    print(S().splitIntoFibonacci(num))
