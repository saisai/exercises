from math import floor, sqrt
def non_square(n):
    return n + floor(1/2 + sqrt(n))

print(*map(non_square, range(1, 23)))

def is_square(n):
    return sqrt(n).is_integer()

non_squares = map(non_square, range(1, 10 ** 6))
next(filter(is_square, non_squares))

