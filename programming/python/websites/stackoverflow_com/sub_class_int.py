

class CustomInt(int):

    def __call__(self,v):
        return CustomInt(self + v)

def add(v):
    return CustomInt(v)

print(add(1))
print(add(1)(2))
print(add(1)(2)(30))

add2 = CustomInt

print(add2(1))
print(add2(1)(2))
print(add2(1)(2)(30))

# https://stackoverflow.com/questions/39038358/function-chaining-in-python
