'''
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/901667/python-3-one-pass-greedy-explanation

Explanation
    Count the frequency of number 1-6 inclusive
        cnt: total apperence for A[i] and B[i], count once if A[i] == B[i], because same value at the same position will cause repeat, e.g.
            A = [1,2,2], B = [1,2,2], there are four 2s in total, but you still can't make the equal row.
        a_cnt: total apperence for each A[i]
        b_cnt: total apperence for each A[i]
    After one pass, for each value in 1 to 6
        if cnt[i] >= n, meaning there is enough i+1 for swapping for make a equal row
        get the minimum of
            n-a_cnt[i]: how many swaps needed to make row A with all same value of i+1
            n-b_cnt[i]: how many swaps needed to make row A with all same value of i+1
Implementation

'''

from typing import List

class S:

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        cnt = [0] * 6
        a_cnt = [0] * 6
        b_cnt = [0] * 6
        for a, b in zip(A, B):
            if a != b:
                cnt[b-1] += 1
            b_cnt[b-1] += 1
            cnt[a-1] += 1
            a_cnt[a-1] += 1
        ans = n
        for i, val in enumerate(cnt):
            if val >= n:
                ans = min(ans, n-a_cnt[i], n-b_cnt[i])
        return ans if ans != n else -1

tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(S().minDominoRotations(tops, bottoms))
