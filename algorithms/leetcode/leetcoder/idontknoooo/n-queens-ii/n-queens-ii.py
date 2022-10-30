"""
https://www.youtube.com/watch?v=nalYyLZgvCY&ab_channel=NeetCode
https://leetcode.com/problems/n-queens-ii/
"""

res = 0
class S:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        #res = 0
        print('out ', id(res))
        def backtrack(r):
            if r == n:
                #nonlocal res  
                global res 
                print('in ', id(res))     
                res += 1
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r -c ) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        backtrack(0)
        return res
n = 4
print(S().totalNQueens(n))
