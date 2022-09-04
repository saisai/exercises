
'''
https://leetcode.com/problems/design-an-atm-machine/
https://leetcode.com/problems/design-an-atm-machine/discuss/1957787/python-3-greedy-pre-authorize-explanation
'''
from typing import List

class ATM:

    def __init__(self):
        self.d = [0] * 5
        self.value = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.d = [a + b for a, b in zip(self.d, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        pre = [0] * 5
        for i in range(4, -1, -1):
            pre[i] = min(self.d[i], amount // self.value[i]) # set up pre-authorize list
            amount -= pre[i] * self.value[i]
            if not amount: break
        else:
            return [-1]
        self.d = [a - b for a, b in zip(self.d, pre)] # once fully verified, decrement the number of bills
        return pre

atm = ATM()
atm.deposit([0, 0, 1, 2, 1])
print(atm.withdraw(600))
atm.deposit([0, 1,0,1,1])
print(atm.withdraw(600))
atm.withdraw(550)


