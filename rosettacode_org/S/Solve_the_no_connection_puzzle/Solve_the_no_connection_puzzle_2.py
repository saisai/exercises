
from __future__ import print_function
from itertools import permutations
from enum import Enum

A, B, C, D, E, F, G, H = Enum('Peg', 'A, B, C, D, E, F, G, H')

connections = ((A, C), (A, D), (A, E),
               (B, D), (B, E), (B, F),
               (G, C), (G, D), (G, E),
               (H, D), (H, E), (H, F),
               (C, D), (D, E), (E, F))


def ok(conn, perm):
    """Connected numbers ok?"""
    this, that = (c.value - 1 for c in conn)
    return abs(perm[this] - perm[that]) != 1


def solve():
    return [perm for perm in permutations(range(1, 9))
            if all(ok(conn, perm) for conn in connections)]

def pp(solution):
    """Prettyprint a solution"""
    boardformat = r"""
         A   B
        /|\ /|\
       / | X | \
      /  |/ \|  \
     C - D - E - F
      \  |\ /|  /
       \ | X | /
        \|/ \|/
         G   H"""

    for letter, number in zip("ABCDEFGH", solution):
        boardformat = boardformat.replace(letter, str(number))
    print(boardformat)

if __name__ == '__main__':
    solutions = solve()
    for i, s in enumerate(solutions, 1):
        print("\nSolution", i, end="")
        pp(s)
