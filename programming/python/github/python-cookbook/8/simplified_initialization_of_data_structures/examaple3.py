
class Structure:

    # Class variable that specifies expected fields

    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError(f'Exptected {len(self._fields)}')

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs: 
            raise TypeError(f'Duplicate values for {*kwargs,}')

if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    print(s1.name)

    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')

