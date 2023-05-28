

def smallestTrimmedNumbers(A, Q):
    m, n = len(A[0]), len(A)
    d = [list(range(n))]
    for i in range(m-1, -1, -1):
        prev_rk = {x:j for j, x in enumerate(d[-1])}
        d.append(sorted(range(n), key=lambda x: (A[x][i], prev_rk[x])))
    return [d[t][k-1] for k, t in Q]


nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]

print(smallestTrimmedNumbers(nums, queries))
