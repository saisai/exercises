
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

https://leetcode.com/problems/valid-parentheses/
https://www.youtube.com/watch?v=WTzjTskDFMg&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&ab_channel=NeetCode

'''
class S:

    def __call__(self, s):
        stack = []
        closeToOpen = {")": "(",
                "]":"[",
                "}": "{"
                }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        return True if not stack else False

if __name__ == '__main__':

    s = "()"
    print(S()(s))
    print(S()("()[]{}"))
    print(S()("(]"))