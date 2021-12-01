import math

def squareFree(_number):
    max = (int) (math.sqrt(_number))
    for root in range(2, max+1):
        if 0 == _number % (root * root):
            return False
    return True

def listSquareFrees(_start, _end):
    count = 0
    for i in range(_start, _end+1):
        if True == squareFree(i):
            print("{}\t".format(i), end="")
            count += 1
    print ( "\n\nTotal count of square-free numbers between {} and {}: {}".format(_start, _end, count))

listSquareFrees(1, 100)
listSquareFrees(1000000000000, 1000000000145)
