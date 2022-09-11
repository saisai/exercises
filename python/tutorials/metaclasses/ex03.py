from collections import OrderedDict

class OrderedType(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return OrderedDict()
    def __new__(cls, name, bases, namespace, **kwargs):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result

class OrderedMethodsObject(object, metaclass=OrderedType):
    def method1(self): pass
    def method2(self): pass
    def method3(self): pass


print(OrderedMethodsObject.members)

# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
