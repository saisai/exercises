'''
https://leetcode.com/problems/prime-palindrome/discuss/1488677/python-3-brute-force-math-pruning-explanation
https://leetcode.com/problems/prime-palindrome/

Explanation
    Filtering out palindrome is very simple, but instead of filtering, we need to make up palindrome in order, so that we don't waste on trying definitely useless numbers.
        Make sure odd digits palindrome and even digits palindrome are both included.
Other than making up palindrome, we can use math to filter values, below are not prime for sure
    Have factor 5: 5xxx5, 5xx5, everything start with 5
    Have factor 2: 2xx2, 4xx4, 6xx6, 8xx8 everything starts with 2, 4, 6, 8

Implementation

'''

class S:

    def primePalindrome(self, n: int) -> int:
        def is_prime(n):
            if n == 1: return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0: return False
            return True

        n_str = str(n)
        l = len(n_str)
        for k in range(max(0, l//2-1), 5):
            for i in range(10**k, 10**(k+1)): # odd length
                i_str = str(i)
                if k > 0 and i_str[0] in ['2', '4', '5', '5', '8']: continue # pruning
                cur = i_str + i_str[-2::-1]
                cur_int = int(cur)
                if cur_int >= n and is_prime(cur_int):
                    return cur_int

            for i in range(10**k, 10**(k+1)): # even length
                i_str = str(i)
                if i_str[0] in ['2', '4', '5', '6', '8']: continue # pruning
                cur = i_str + i_str[::-1]
                cur_int = int(cur)
                if cur_int >= n and is_prime(cur_int):
                    return cur_int
        return -1

n = 6
print(S().primePalindrome(n))
