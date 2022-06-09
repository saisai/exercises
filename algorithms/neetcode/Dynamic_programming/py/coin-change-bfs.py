
from collections import deque
class S:

    def __call__(self, coins, amount):

        deq = deque([(amount, 0)])
        visited = set()
        while deq:
            t, cnt = deq.popleft()

            if t == 0:
                return cnt
            for val in coins:
                sub = t - val
                if sub >= 0:
                    if sub not in visited:
                        visited.add(sub)
                        deq.append((sub, cnt + 1))
        return -1

'''
coins = [1,2,5]
amount = 11

print(S()(coins, amount))
'''
coins = [2]
amount = 3
print(S()(coins, amount))



