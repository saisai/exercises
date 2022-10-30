'''
https://leetcode.com/problems/length-of-last-word/
https://leetcode.com/problems/length-of-last-word/solutions/848177/python-3-two-methods-iterative-split-explanations/
'''

class S:

    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        for i in range(n-1, -1, -1):        # find non-empty char from right
            if s[i] != ' ': break
        else: return 0
        tmp_i = i
        for i in range(tmp_i - 1, -1, -1):  # count word length
            if s[i] == ' ': return tmp_i - i # if there are more characters before s[i]
        return tmp_i - i + 1                # if reach to the most left side (i == 0)


for s in ["Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy"]:
    print(S().lengthOfLastWord(s))
