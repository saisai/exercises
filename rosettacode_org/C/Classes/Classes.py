class MyClass:

    name2 = 2 # class attribute


    def __init__(self):
        """
        Constructor  (Technically an initializer rather than a true "constructor")
        """
        self.name1 = 0 # Instance attribute

    def some_method(self):
        """
        Method
        """
        self.name1 = 1
        MyClass.name2 = 3

myclass = MyClass() # class name, invoked as a function is the constructor syntax.
print(myclass.name2)
myclass.name2 = "test"
print(myclass.name2)
print(myclass.name1)
myclass.name1 = 'tt'
print(myclass.name1)

print(MyClass.name2)
MyClass.name2 = 'hello'
print(MyClass.name2)

MyClass.name1 = 'aaa'
print(MyClass.name1)
