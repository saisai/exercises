import random 

def gen(N):
    txt = ['[', ']'] * N
    random.shuffle(txt)
    return ''.join(txt)

def balanced(txt):
    braced = 0
    for ch in txt:
        if ch == '[': braced += 1
        if ch == ']':
            braced -= 1
            if braced < 0:  return False
    return braced == 0

for txt in (gen(N) for N in range(10)):
    print('%-22r is %s balacned' % (txt, '' if balanced(txt) else ' not'))
