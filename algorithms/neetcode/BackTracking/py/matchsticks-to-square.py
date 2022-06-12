
class S:

    def __call__(self, matchsticks):
        length = sum(matchsticks) // 4
        sides = [0] * 4

        if sum(matchsticks) / 4 != length:
            return False

        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)

print(S()([1,1,2,2,2]))
print(S()([3,3,3,3,4]))

# https://leetcode.com/problems/matchsticks-to-square/
# https://www.youtube.com/watch?v=hUe0cUKV-YY&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=17&ab_channel=NeetCode