
from typing import List

class S:

    def minStickers(self, stickers: List[str], target: str) -> int:

        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c, 0)

        dp = {} # key = subseq of target  | val = min num of sticekrs

        def dfs(t, stick):
            if t in dp:
                return dp[t]

            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c

            if remainT:
                used = float("inf")

                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                
                res += used

            return res
        res = dfs(target, {})
        return res if res != float("inf") else -1

stickers = ["with","example","science"]
target = "thehat"
print(S().minStickers(stickers, target))

