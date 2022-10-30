'''
658. Find K Closest Elements


Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

https://leetcode.com/problems/find-k-closest-elements/
https://www.youtube.com/watch?v=o-YDQzHoaKM&list=PLot-Xpze53leNZQd0iINpD-MAhMOMzWvO&index=4&ab_channel=NeetCode
'''

class Solution:
    
    def __call__(self, arr, k, x):
        
        l, r = 0, len(arr) - k
        
        while l < r:
            m = ( l + r ) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]
    
arr = [1,2,3,4,5]
k = 4
x = 3
print(Solution()(arr, k, x))