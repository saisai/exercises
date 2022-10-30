'''
https://1e9.medium.com/monotonic-queue-notes-980a019d5793
https://leetcode.com/problems/constrained-subsequence-sum/
https://leetcode.com/problems/constrained-subsequence-sum/discuss/597744/python-on-monoqueue

Consider a typical (but inefficient) DP: we have dp[i] = the max sum of some non-empty subset of nums[..i] that contains nums[i]. The final answer is max(dp).

In this dp, we have the recurrence relation dp[i+K] = nums[i+K] + max(0, dp[i], dp[i+1], ..., dp[i+K-1]). We can use a monoqueue (a queue that supports a O(1) max operation) to efficiently perform this DP - it stores the result of max(...) and we update it by eg. adding dp[i+K+1] and popping dp[i].

'''
import collections

class Monoqueue(collections.deque):

    def enqueue(self, val):
        count = 1
        while self and self[-1][0] < val:
            count += self.pop()[1]
        self.append([val, count])

    def dequeue(self):
        ans = self.max()
        self[0][1] -= 1
        if self[0][1] <= 0:
            self.popleft()
        return ans

    def max(self):
        return self[0][0] if self else 0


class S:
    def constraintSubsetSum(self, A, K):
        monoq = Monoqueue()
        ans = max(A)
        for i, x in enumerate(A):
            monoq.enqueue(x + max(0, monoq.max()))
            if i >= K:
                ans = max(ans, monoq.dequeue())
        return max(ans, monoq.dequeue())

A= [10,2,-10,5,20]
K = 2
print(S().constraintSubsetSum(A, K))
