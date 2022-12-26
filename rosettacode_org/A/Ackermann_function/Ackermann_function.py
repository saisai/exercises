
import sys
from functools import lru_cache

def ack1(M, N):
    return (N + 1) if M == 0 else (
            ack1(M-1, 1) if N == 0 else ack1(M-1, ack1(M, N-1))
            )

@lru_cache(None)
def ack2(M, N):
    if M == 0:
        return N + 1
    elif N == 0:
        return ack2(M - 1, 1)
    else:
        return ack2(M - 1, ack2(M, N - 1))

sys.setrecursionlimit(3000)
print(ack1(0,0))
print(ack1(3, 4))
print(ack2(0, 0))
print(ack2(3, 4))

def ack2(M, N):
   return (N + 1)   if M == 0 else (
          (N + 2)   if M == 1 else (
          (2*N + 3) if M == 2 else (
          (8*(2**N - 1) + 5) if M == 3 else (
          ack2(M-1, 1) if N == 0 else ack2(M-1, ack2(M, N-1))))))

