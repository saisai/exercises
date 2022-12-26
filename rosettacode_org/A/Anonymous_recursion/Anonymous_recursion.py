Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
fib = lambda f: lambda n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(n-1) + f(n-2)))

t = [Y(fib)(i) for i in range(-2, 10)]
print(t)


from functools import partial

YY = lambda f: (lambda x: x(x))(lambda y: partial(f, lambda *args: y(y)(*args)))
fib = lambda f, n: None if n < 0 else (0 if n == 0  else (1 if n == 1 else f(n-1) + f(n-2)))
tt = [YY(fib)(i) for i in range(-2, 10)]
print(tt)


YYY = lambda f: partial(f, f)
fib = lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(f, n-1) + f(f, n-2)))
t1 = [YYY(fib)(i) for i in range(-2, 10)]
print(t1)


from inspect import currentframe
from types import FunctionType
def myself(*args, **kw):
    caller_frame = currentframe(1)
    code = caller_frame.f_code
    return FunctionType(code, caller_frame.f_globals)(*args, **kw)

print("factorial(5) =")
print(lambda n: 1 if n <= 1 else n * myself(n-1, 5))


Y = lambda f: lambda n: f(f,n)
fib = lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(f,n-1) + f(f,n-2))) #same as the first three implementations

t = [ Y(fib)(i) for i in range(-2, 10) ]
print(t)


fib_func = (lambda f: lambda n: f(f,n))(lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(f,n-1) + f(f,n-2))))
t = [ fib_func(i) for i in range(-2, 10) ]
print(t)
