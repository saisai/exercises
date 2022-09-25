'''
https://leetcode.com/problems/closest-dessert-cost/
https://leetcode.com/problems/closest-dessert-cost/discuss/1085928/python-3-backtracking-dfs-explanation

Explanation
    There will be 10 bases at most and 10 toppings at most, you can choose among (0, 1, 2) amount of each topping type. In total, maximum, there will be 10 * (3 ^ 10) = 590490 combinations.
    Since 590490 is less than 10^3 * 10^3 (experience), it's total doable to try out all 590490 combinations
    Use backtracking to test out all the combination and find out the cloest one based on rules
    ans is a tuple contains these information, ans = (total_cost, absolute_difference, less/equal/greater_than_target)
    Starting with [0] * m, try out all possibilities

Implementation

'''
from typing import List

class S:

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        m = len(toppingCosts)
        ans = (baseCosts[0], abs(baseCosts[0]-target), -1 if target > baseCosts[0] else (0 if target == baseCosts[0] else 1))

        def dfs(cnt, cur_idx):
            nonlocal ans, m, base
            if cur_idx >= m: return
            for i in range(3):
                cnt[cur_idx] = i
                if cur_idx >= m: return
                s = sum([tc * c for tc, c in zip(toppingCosts, cnt)]) + base
                diff = abs(target - s)
                sign = -1 if target > s else (0 if target == s else 1)
                if not diff: ans = (target, 0, 0); return
                if diff < ans[1]: ans = (s, diff, sign)
                elif diff == ans[1] and ans[2] == 1 and sign == -1: ans = (s, diff, sign)
                dfs(cnt[:], cur_idx+1)

        for base in baseCosts:
            dfs([0] * m, 0)
        return ans[0]

baseCosts = [1,7]
toppingCosts = [3,4]
target = 10

print(S().closestCost(baseCosts, toppingCosts, target))
