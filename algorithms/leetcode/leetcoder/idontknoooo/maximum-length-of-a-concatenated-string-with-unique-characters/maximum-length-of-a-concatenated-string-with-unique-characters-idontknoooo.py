'''

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solutions/872596/python-3-38-backtracking-set-union-walrus-operator-explanation/

I think it's totally reasonable if you don't like or not familiar with Walrus operator (:=), but it does help to make the code shorter. Also, it's not too hard to understand.

Explanation
    Basic idea is to turn arr to [(set(word), len(word))] if word has no repeat letter
    Then we can use union (&) operation to check whether length of set after union is same as the sum of two size
        if (union_len:=len(union:=arr[i][0] | cur_s)) == arr[i][1] + cur_l]
        if len(arr[i][0] | cur_s) == arr[i][1] + cur_l same as above
    Due to the small data sacle (max length of arr is 16), use backtracking to try out all possbilities
    Maintain a maximum length with ans

'''
from typing import List

class S:

    def maxLength(self, arr: List[str]) -> int:
        arr = [(s, l) for word in arr if ( l := len( s := set(word))) == len(word)]
        ans, n = 0, len(arr)
        def dfs(arr, cur_s, cur_l, idx):
            nonlocal ans, n
            ans = max(ans, cur_l)
            if idx == n: return
            [dfs(arr, union, union_len, i+1) for i in range(idx, n)  if (union_len := len(union := arr[i][0] | cur_s)) == arr[i][1] + cur_l]

        dfs(arr, set(), 0, 0)
        return ans
    
arr = ["un","iq","ue"]
print(S().maxLength(arr))