

class Validator(type):
    def __new__(metacls, cls, bases, clsdict):
        for name, attr in clsdict.items():
            print(name, attr)
            if isinstance(attr, ValidateType):
                attr.name = name
                attr.attr = "-" + name
            # create final class and return it
            return super().__new__(metacls, cls, bases, clsdict)

class ValidateType:
    def __init__(self, type):
        self.name = None
        self.attr = None
        self.type = type
    
    def __get__(self, inst, cls):
        if inst is None:
            return self
        else:
            return inst.__dict__[self.attr]

    def __set__(self, inst, value):
        if not isinstance(value, self.type):
            raise TypeError("%s must be of type(s) %s (got %r)" % 
                    (self.name, self.type, value))

        else:
            inst.__dict__[self.attr] = value

class Person(metaclass=Validator):
    weight = ValidateType(int)
    age = ValidateType(int)
    name = ValidateType(str)

p = Person()
p.weight = 5
print(p.weight)


# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
