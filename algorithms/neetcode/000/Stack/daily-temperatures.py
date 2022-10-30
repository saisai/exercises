
'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

https://leetcode.com/problems/daily-temperatures/
https://www.youtube.com/watch?v=cTBiBSnjO3c&list=PLot-Xpze53lfxD6l5pAGvCD4nPvWKU8Qo&index=6&ab_channel=NeetCode
'''
class S:
    
    @classmethod
    def dailyTemperatures(cls, temperatures):
        res = [0] * len(temperatures)
        stack = [] # pari: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
 
temperatures = [73,74,75,71,69,72,76,73]   
print(S.dailyTemperatures(temperatures))
        