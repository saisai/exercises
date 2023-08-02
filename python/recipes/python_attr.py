from threading import local

t = local()
print(dir(t))
print('\n')
setattr(t, 'test', 'abc')
setattr(t, 'tester', 'abcde')

print(dir(t))
print('\n')

print(getattr(t, 'test'))

del t.test 

print(dir(t))
print('\n')

del t.tester 

print(dir(t))
print('\n')


# https://stackoverflow.com/questions/1120927/which-is-better-in-python-del-or-delattr
