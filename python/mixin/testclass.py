class Hello:

    def test(self):
        print('hello')

    def attr(self):
        if hasattr(self, 'test'):
            print('yes')

    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Hello.factorial(number - 1)

h = Hello()
h.attr()


f = Hello.factorial(10)
print(f)