funcs = []
for i in range(10):
    funcs.append(lambda: i * i)
#print(funcs)
print(funcs[3]())
print(funcs[5]())


funcss = []
for i in range(10):
    funcss.append(lambda i=i: i * i)
print(funcss[3]())
print(funcss[5]())


func2 = [lambda i=i: i * i for i in range(10)]
#print(func2)
print(func2[4]())


func3 = list(map(lambda i: lambda: i * i, range(10)))
#print(func3)
print(func3[3]())

func4 = [eval("lambda:%s"%i**2) for i in range(10)]

print(func4)
print(func4[3]())
