def arithmetic(x, y):
    for op in "+ - * // % **".split():
        expr = "%(x)s %(op)s %(y)s" % vars()
        print("%s\t=> %s" % (expr, eval(expr)))


arithmetic(12, 8)
arithmetic(input("Number 1: "), input("Number 2: "))

input1 = 18
# input1 = input()
input2 = 7
# input2 = input()

qq = input1 + input2
print("Sum: 		  " + str(qq))
ww = input1 - input2
print("Difference: 	  " + str(ww))
ee = input1 * input2
print("Product: 	  " + str(ee))
rr = input1 / input2
print("Integer quotient: " + str(int(rr)))
print("Float quotient:   " + str(float(rr)))
tt = float(input1 / input2)
uu = (int(tt) - float(tt)) * -10
# print(tt)
print("Whole Remainder:  " + str(int(uu)))
print("Actual Remainder: " + str(uu))
yy = input1 ** input2
print("Exponentiation:   " + str(yy))