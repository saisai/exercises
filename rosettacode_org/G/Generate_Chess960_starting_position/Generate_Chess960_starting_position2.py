import re
from itertools import permutations

pieces = 'KQRRBBNN'
bish = re.compile(r'B(|..|....|......)B').search 
king = re.compile(r'R.*K.*R').search 
starts3 = {p for p in (''.join(q) for q in permutations(pieces))
           if bish(p) and king(p)}
print(len(starts3))
print(starts3.pop())

