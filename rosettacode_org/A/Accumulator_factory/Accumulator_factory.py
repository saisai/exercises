def accumulator(num):
    def f(n):
        f.num += n
        return f.num
    f.num = num
    return f

x = accumulator(1)
print(x(5))
print(x(2.3))
