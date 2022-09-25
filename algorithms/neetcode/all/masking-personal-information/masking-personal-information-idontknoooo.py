'''
https://leetcode.com/problems/masking-personal-information/
https://leetcode.com/problems/masking-personal-information/discuss/1426661/python-3-f-string-explanation-this-should-be-an-easy-question

'''
class S:

    def maskPII(self, s: str) -> str:
        if '@' in s:
            user, domain = s.split('@')
            return f'{user[0].lower()}{"*"*5}{user[-1].lower()}@{domain.lower()}'
        else:
            s = ''.join([c for c in s if c.isdigit()])
            n = len(s)
            return f'+{"*"*(n-10)}-***-***-{s[-4:]}' if n != 10 else f'***-***-{s[-4:]}'

s = "AB@qq.com"
print(S().maskPII(s))

