'''

https://leetcode.com/problems/break-a-palindrome/
https://leetcode.com/problems/break-a-palindrome/solutions/846873/python-3-greedy-one-pass-explanations/

Explanation
    If length of palindrome == 1, return ''
    For even length string, if we found a char that is not a, replace it with a and return
    For odd length string, if we find a char that is not a and it's not the middle of string, replace it with a and return
    If all a in the string, replace the last char to b
Implementation
'''
class S:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ''
        for i, c in enumerate(palindrome):
            if c != 'a' and (( i != n // 2 and n % 2) or not n % 2): return palindrome[:i] + 'a' + palindrome[i+1:]
        else: return palindrome[:-1] + 'b'

palindrome = "abccba"
print(S().breakPalindrome(palindrome))
