

def stripchars(s, chars):
    return "".join(c for c in s if c not in chars)

print(stripchars("She was a soul stripper. Shw took my heart!", "aei"))


