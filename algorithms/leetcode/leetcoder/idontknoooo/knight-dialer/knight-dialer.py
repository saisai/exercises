'''
https://leetcode.com/problems/knight-dialer/
https://leetcode.com/problems/knight-dialer/solutions/833421/python-3-dfs-memoization-symmetry-explanation/

'''
class S:
    d = [(4,6),(6,8),(7,9),(4,8),(3,9,0),(),(1,7,0),(2,6),(1,3),(2,4)]       # Create a graph, index is the vertex and values are the edges
    cache = {}
    def dfs(self, i, n):
        if n == 0: return 1
        elif (i, n) not in self.cache:
            self.cache[i, n] = sum(self.dfs(val, n-1) for val in self.d[i]) # Memoization
            if i in [1, 4, 7]: self.cache[i+2, n] = self.cache[i, n]        # Symmetry
            elif i in [3, 6, 9]: self.cache[i-2, n] = self.cache[i, n]

    def knightDialer(self, n: int) -> int:
        print("n ", n)
        return sum(self.dfs(i, n-1) for i in range(10)) % (int(1e9)+7)
'''
for j in [1, 2, 3131]:
    #print(i)
    print(S().knightDialer(j))
'''
print(S().knightDialer(2))

