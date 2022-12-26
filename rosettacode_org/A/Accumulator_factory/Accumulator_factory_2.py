
def accmulator(num):
    def f(n):
        nonlocal num
        num += n
        return num
    return f

x = accmulator(1)
x(5)
print(accmulator(3))
print(x(2.3))
