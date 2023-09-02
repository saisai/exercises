

class Hello:
    cache_keys = ('test', 'hello', 'world')

    def __init__(self):
        test = "test"

    def hello(self):
        print("Hello")

t = Hello()
#t.hello()

for k in getattr(t, 'cache_keys', []):
    print(k)

print(getattr(t, 'cache_keys'))

