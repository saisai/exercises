
def accumulator(num):
    while True:
        num += yield num

x = accumulator(1)
x.send(None)
x.send(5)
print(accumulator(3))
print(x.send(2.3))
