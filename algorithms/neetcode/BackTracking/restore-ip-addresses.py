import pdb
class S:
    @staticmethod
    def restoreIpAddresses(s):
        # 256 choices for each of the 4 spots BUT...
        # The order of s statys same,
        # we just place the "." in between
        res = []
        if len(s) > 12:
            return res
        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s): # remove last char "."
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                print('j ', j, ' -> i', i, ' dots -> ', dots)
                if int(s[i:j+1]) < 256 and (i == j or s[i] != '0'):
                    backtrack(j + 1, dots + 1, curIP + s[i:j+1] + ".")
        backtrack(0, 0, "")
        return res
print(S().restoreIpAddresses("25525511135"))

# https://leetcode.com/problems/restore-ip-addresses/
# https://www.youtube.com/watch?v=61tN4YEdiTM&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=16&ab_channel=NeetCode