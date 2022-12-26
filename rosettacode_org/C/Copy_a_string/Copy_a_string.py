src = "hello"
a = src
b = src[:]
print(a)
print(b)
import copy
c = copy.copy(src)
d = copy.deepcopy(src)
t = src is a is b is c is d
print(t)

a = "hello"
b = ''.join(a)
print(a == b)
print(b is a)
