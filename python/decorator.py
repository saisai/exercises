
def hello(name):
    def hello_name(age,sex):
        return "I am %s and %d and %s" % (name, age, sex)
    return hello_name

# 1
h = hello("John")
print(h(25, "Male"))

# 2
print(hello("Nancy")(25, "Female"))

def hello2(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@hello2
def hello_test_2():
    print("I am Honey, 25, Male")
hello_test_2()


@hello2
def hello_test_3(name, age, sex):
    print("I am %s and %d and %s" % (name, age, sex))
hello_test_3("Alex", 30, "Male")


# return value from the inner function
def hello3(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper

@hello3
def hello_test_3():
    print("I am Honey, 25, Male")
    return 3
t = hello_test_3()
print(t)

@hello3
def hello_test_33(name, age, sex,option):
    print("I am %s and %d and %s" % (name, age, sex))
    return 34
t = hello_test_33("Alex", 30, "Male", option="check")
print(t)

print(hello3(hello_test_33)("Alex", 30, "Male", option="check2"))

