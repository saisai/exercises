def multiply(a, b):
    return a * b


print(multiply(10, 10))


multiply_1 = lambda a, b: a * b

print(multiply_1(10, 10))


class Multiply:

    def __init__(self):
        pass

    def __call__(self, a, b):
        return a * b


multiply = Multiply()
print(multiply(10, 10))
