class MyOtherClass:
    count = 0  # Population of "MyOtherClass" objects
    def __init__(self, name, gender="Male", age=None):
        """
        One initializer required, others are optional (with different defaults)
        """
        MyOtherClass.count += 1
        self.name = name
        self.gender = gender
        if age is not None:
            self.age = age
    def __del__(self):
        MyOtherClass.count -= 1
        
        
person1 = MyOtherClass("John")
print(person1.name, person1.gender)  # "John Male"
try:
    print(person1.age)                   # Raises AttributeError exception!
except AttributeError as e:
    print(e)
print(person1.count)
person2 = MyOtherClass("Jane", "Female", 23)
print(person2.count)
person3 = MyOtherClass("Jane", "Female", 23)
print(person2.name, person2.gender, person2.age)  # "Jane Female 23"        
print(person3.count)
print(MyOtherClass.count)