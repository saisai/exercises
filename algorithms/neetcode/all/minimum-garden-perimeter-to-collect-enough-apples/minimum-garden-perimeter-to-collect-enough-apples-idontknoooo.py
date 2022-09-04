'''
https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/discuss/1440075/python-3-binary-search-math-ologn-explanation

Explanation
    Center row will be p, p-1, p-2, ..., 0, ..., p-2, p-1, p
    One row above the center row is p+1, p, p-1, ..., 0, ..., p-1, p, p+1
    Then you can calculate the total apple counts given p using Arithmetic Progression
        sum = (first + last) * n // 2

Implementation
'''
class S:

    def minimumPerimeter(self, neededApples: int) -> int:
        def ok(p):
            center = p * (p+1)
            base = center + (p*2+1)
            last = base + (p*2+1) * (p-1)
            total = (base + last) * p + center
            return total >= neededApples

        l, r = 1, int(1e5)
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid - 1
            else:
                l = mid + 1
        return 4*2*1

neededApples = 1
print(S().minimumPerimeter(neededApples))
