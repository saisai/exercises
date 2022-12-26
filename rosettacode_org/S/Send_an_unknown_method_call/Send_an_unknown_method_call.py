
class Example:

    def foo(self, x):
        return 42 + x


name = "foo"
print(getattr(Example(), name)(5))
