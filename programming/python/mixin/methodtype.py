class MethodTypes:

    name = "Ragnar"

    def __init__(self):
        self.age = 20

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")

print(dir(MethodTypes))

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()

print(MethodTypes.name)
print(m.age)


MethodTypes.classMethod()
MethodTypes.staticMethod()

# https://levelup.gitconnected.com/method-types-in-python-2c95d46281cd
# https://gist.github.com/gmotzespina/956dc7556637801fb7250d3d2250fc2f#file-math-py
# https://realpython.com/instance-class-and-static-methods-demystified/
# https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call