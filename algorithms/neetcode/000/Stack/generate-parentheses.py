'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

https://leetcode.com/problems/generate-parentheses/
https://www.youtube.com/watch?v=s9fokUqJ76A&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=4&ab_channel=NeetCode
'''

class S:
    
    def __call__(self, n):
        
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
                
        backtrack(0,0)
        return res 
    
print(S()(3))

# https://www.youtube.com/watch?v=s9fokUqJ76A&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=4&ab_channel=NeetCode