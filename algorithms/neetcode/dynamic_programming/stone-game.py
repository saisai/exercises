

from typing import List

class S:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # subarr piles (l, r) -> Max Alice Total

        # Return: Max Alice Total
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            even = True if (r - l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            dp[(l, r)] = max(dfs(l + 1, r) + left,
                         dfs(l, r - 1) + right)
            return dp[(l, r)]
        return dfs(0, len(piles) -1 ) > (sum(piles)) // 2

piles = [5,3,4,5]
print(S().stoneGame(piles))

