# example 1
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

"""
say_whees = my_decorator(say_whee)
say_whees()
print()
my_decorator(say_whee)()
"""

# example 2

def my_decorator2(func):
    def wrapper2(test):
        print("Something is happening before the function is called.")
        func(test)
        print("Something is happening after the function is called.")
    return wrapper2

def say_whee2(param):
    print(param)

"""
say_whees2 = my_decorator2(say_whee2)
say_whees2('test')
print()
my_decorator2(say_whee2)('test')
"""


def my_decorator3(func):
    def wrapper3(test):
        print("Something is happening before the function is called.")
        func(test)
        print("Something is happening after the function is called.")
    #return wrapper2
    return lambda testt: wrapper3(testt)

def say_whee3(param):
    print(param)

say_whees3 = my_decorator3(say_whee3)
say_whees3('tester')
print()
my_decorator3(say_whee3)('tester')

# lambda 
print()
t = lambda x: x 
print(t('t'))


print()
tt = lambda a, b: (a + b) 
print(tt(1, 2))

print()
def lambfunc():
    print("tt")
    
def lambfunc2(param):
    print(param)    
    
tt3 = lambda a: a 
tt3(lambfunc)()
tt3(lambfunc2)('hello')

print('a')
tt4 = lambda a, b: (a, b )
tt4(lambfunc, lambfunc2)[1]('tt')

print('b')
tt4 = lambda a, b: (a, b )
#tt4(lambfunc2, lambfunc2)[1]('aa')

for i in range(0, 2):
    tt4(lambfunc2, lambfunc2)[i]('aa ' + str(i))
    
print()
print('c')    
def xShow(a):
    print("x hello " + a)
    
def yShow():
    print('y hello')
    
def go(x, y):
    return x, y
    
c = lambda xshow: lambda yshow: go(xshow, yshow)

c(xShow)(yShow)[0]("test")
c(xShow)(yShow)[1]()



# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    print(g)
    '''Right to left function composition.'''
    return lambda f: g(f)
    #return lambda f: lambda x: g(f(x))
    
    
#t = compose(len)(list)('abc')
t = compose(len)('abc')
print(t)

def compose2(g):

    def test(val):
        return g(val)
    return test 
    
tt = compose2(len)('abc')
print(tt)

tt3 = compose2(len)
print(tt3('abc'))


def compose3(g):
    print(g)
    '''Right to left function composition.'''
    
    #return lambda f: lambda x: g(f(x))
    return lambda f: lambda x: g(f(x))
    
#               g   f      x    
ttt = compose3(len)(list)(['a', 'b'])
print(ttt)

print('aa')

def compose33(g):
    print(g)
    
    def ff(ll):
        print(ll)
        def gg(x):
            print(x)
            #return ll(x)
            return g(ll(x))
        
        return gg
        
    return ff

ttt1 = compose33(len)(list)('abc')

print(ttt1)
"""
def xxShow(ss):
    return ss.upper()

def test():
    
    
        def go(xShow):
            print(s)
            return xShow(t)
    #return lambda xShow: go(str)
        return lambda xShow: go(xxShow)
    return go

print(test()('t')())
#print(test('hello')())
"""