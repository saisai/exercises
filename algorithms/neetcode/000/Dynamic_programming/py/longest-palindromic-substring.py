
class S:

    def __call__(self, s):        
        res = ""
        resLen = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 ) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( r - l + 1) > resLen:
                    res = s[l:r+ 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

class SS:

    def __call__(self, s):

        maxlen = float("-inf")
        stack = []
        N = len(s)

        for i in range(2 * N - 1):
            l = i // 2
            r = (i + 1 ) // 2

            while l >= 0 and r < N and s[l] == s[r]:
                curlen = r - l + 1
                if curlen> maxlen:
                    maxlen = curlen
                    stack.append(s[l:r+1])

                l -= 1
                r += 1
        return stack.pop()

s = "babad"
print(SS()(s))
