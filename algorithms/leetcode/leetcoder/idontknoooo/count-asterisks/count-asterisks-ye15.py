'''
https://leetcode.com/problems/count-asterisks/discuss/2195867/python3-1-line
https://leetcode.com/problems/count-asterisks/

'''
class S:
    def countAsterisks(self, s: str) -> int:

        return sum(w.count('*') for i, w in enumerate(s.split('|')) if not i&1)

s = "l|*e*et|c**o|*de|"

print(S().countAsterisks(s))
