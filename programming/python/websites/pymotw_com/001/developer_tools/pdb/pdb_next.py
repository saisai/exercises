import pdb


def calc(i, n):
    j = i * n
    return j


def f(n):
    for i in range(n):
        j = calc(i, n)
        print(i, j)
    return

if __name__ == '__main__':
    pdb.set_trace()
    f(5)