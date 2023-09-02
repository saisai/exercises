
def apply(n):
    def go(f):
        return f(n)
    return lambda f: go(f)
print('a ', apply(3)(range))
print('a ', list(apply(3)(range)))
print('a ', apply(3)(range)[2])


def apply2(n):
    print(type(n))
    def go(f, g, h):
        print('f ', type(f), f)
        print('g ', type(g), g)
        return h(g(f(n)))
    # call  int , range, list
    return lambda f: lambda g: lambda h: go(f, g, h)

print('b ', apply2('3')(int)(range)(list))


# tail :: [a] -> [a]
def tail(xs):
    return xs[1:]


# init::[a] - > [a]
def init(xs):
    return xs[:-1]


def compose(g):
    return lambda f: lambda x: g(f(x))

print(compose(init)(tail)('abcdef'))
print(compose(init)(tail)(range(10)))
print(list(range(10)))

# tail :: [a] -> [a]
def tail_z(xs):
    return xs[1:]

# init::[a] - > [a]
def init_z(xs):
    return xs[:-1]

def list_z(xs):
    print('test ', list(xs))
    #return list(xs)
    return xs

def compose_z(g):
    return lambda f: lambda x: lambda z: lambda y: g(f(x(z(y))))

print(compose_z(tail_z)(init_z)(list_z)(tuple)('abcdef'))
print(compose_z(tail_z)(init_z)(list_z)(list)('abcdef'))
print(compose_z(tail_z)(init_z)(list_z)(tuple)(range(1, 10)))
print(compose_z(tail_z)(init_z)(list_z)(list)(range(1, 10)))
