def accumulator(summer):
    def f(n):
        print('n ', n)
        print('f.summer ', f.summer)
        f.summer += n
        print(f.summer)
        return f.summer
    f.summer = summer
    return f

x = accumulator(1)
print(x(5))
print(x(2.3))

