def reps(text):
    return [text[:x] for x in range(1, 1 + len(text) // 2)
            if text.startswith(text[x:])]

matchstr = """\
1001110011
1110111011
0010010010
1010101010
1111111111
0100101101
0100100
101
11
00
1
"""

print('\n'.join('%r has reps %r' % (line, reps(line)) for line in matchstr.split()))