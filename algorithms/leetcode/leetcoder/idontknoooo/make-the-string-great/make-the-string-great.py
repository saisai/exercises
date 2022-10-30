'''
https://leetcode.com/problems/make-the-string-great/
https://leetcode.com/problems/make-the-string-great/solutions/781226/python-3-stack-on/
'''
class S:

    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or abs(ord(stack[-1]) - ord(c)) != 32:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)


for s in ["leEeetcode", "abBAcC"]:
    print(S().makeGood(s))
