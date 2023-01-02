
class S:

    @classmethod
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s i, i + 1)

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
        

    def working():

        res = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

s = "abc"
print(S.countSubstrings(s))
