'''
https://leetcode.com/problems/additive-number/
https://leetcode.com/problems/additive-number/discuss/1482525/python-3-iterative-simulation-explanation

'''
class S:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)
        def to_the_end(a, b, i):
            nonlocal n, num
            c, c_str = a+b, str(a+b)    # sort of do-while loop
            c_1 = len(c_str)
            while i+ c_1 <= n and num[i:i+c_1] == c_str:
                a, b = b, c
                c, c_str = a+b, str(a+b)
                i, c_1 = i+c_1, len(c_str)
            return i == n                   # when index reach to the end

        for i in range(1, n):               # try out all first value possibilites
            if i > 1 and num[0] == '0': break   # leading zero non-zero number, like '02'
            first = int(num[:i])
            for j in range(i+1, n):         # try out all second value possibilities
                if j > i+1 and num[i] == '0': break # leading zero non-zero number, like '02'
                second = int(num[i:j])
                if to_the_end(first, second, j):    # given first & second str, see if it can reach to the end
                    return True
        return False

num = "199100199"
print(S().isAdditiveNumber(num))
