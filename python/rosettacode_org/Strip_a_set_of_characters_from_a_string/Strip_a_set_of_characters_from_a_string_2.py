import re
import string

def stripchars(s, chars):
    return s.translate(string.maketrans("", ""), chars)

print(stripchars("She was a soul stripper. She took my heart!", "aei"))
