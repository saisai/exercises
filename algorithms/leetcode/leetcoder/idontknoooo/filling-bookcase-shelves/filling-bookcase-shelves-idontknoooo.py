'''
Explanation
dp[i]: Minimum height sum for the first i books
Given the ith book, we just need to decide whether
    It's gonna be on its own row, or
    Append to some previous row
We can find out above with a nested loop O(N*N)
Time: O(N*N)
Space: O(N)
Implementation

https://leetcode.com/problems/filling-bookcase-shelves/
https://leetcode.com/problems/filling-bookcase-shelves/discuss/1517001/python-3-dp-explanation

'''
import sys
from typing import List

class S:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)
        dp = [sys.maxsize] * n

        dp[0] = books[0][1]         # first book will always on it's own row
        for i in range(1, n):       # for each book
            cur_w, height_max = books[i][0], books[i][1]
            dp[i] = dp[i-1] + height_max    # initialize result for current books `dp[i]`
            for j in range(i-1, -1, -1):    # for each previous `book[j]` verify if it can be placed in the same row as `book[i]`
                if cur_w + books[j][0] > shelfWidth: break
                cur_w += books[j][0]
                height_max = max(height_max, books[j][1]) # update current max height
                dp[i] = min(dp[i], (dp[j-1] + height_max) if j - 1 >= 0 else height_max) # always tatke the maximum heigh on current row
        return dp[n-1]

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
print(S().minHeightShelves(books, shelfWidth))
