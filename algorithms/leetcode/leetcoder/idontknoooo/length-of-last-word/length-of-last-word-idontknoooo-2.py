'''
https://leetcode.com/problems/length-of-last-word/
https://leetcode.com/problems/length-of-last-word/solutions/848177/python-3-two-methods-iterative-split-explanations/
'''

class S:

    def lengthOfLastWord(self, s: str) -> int:
        s = [word for word in s.split(' ') if word]
        return len(s[-1]) if s else 0


for s in ["Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy"]:
    print(S().lengthOfLastWord(s))
