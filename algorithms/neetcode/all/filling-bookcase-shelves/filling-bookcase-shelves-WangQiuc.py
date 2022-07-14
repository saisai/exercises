'''
It's a kind of 2D knapsack problem.
The core recurrence function is dp[i+1] = min(dp[k] + h for k in {j+1,...,i}).

j is the furthest index that {books[j+1],...,books[i]} can be placed in one row. It depends on the widths of those books. books[j] can't be placed into the same row with books[i] otherwise the width would exceed the shelf_width.
k is each candidate index that {{books[k],...,books[i]}} are proposed to be placed in the same row.
h is the maximum height among {books[k],...,books[i]}.


https://leetcode.com/problems/filling-bookcase-shelves/discuss/323350/Python-Clean-DP-Solution-2D-Knapsack

https://leetcode.com/problems/filling-bookcase-shelves/
'''


def minHeightShelves(books, shelf_width):

    dp = [0]
    for i in range(len(books)):
        w, j = books[i][0], i
        while j >= 0 and w <= shelf_width: # find out j ,so w should be ahead of j
            j -= 1
            w += books[j][0]
        dp.append(min(dp[k]+ max(books[x][1] for x in range(k, i +1)) for k in range(j+1, i+1)))
    return dp[-1]

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(minHeightShelves(books, shelf_width))
