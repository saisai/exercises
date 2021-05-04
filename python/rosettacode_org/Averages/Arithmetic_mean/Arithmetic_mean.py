from math import fsum
def average(x):
    return fsum(x)/float(len(x)) if x else 0
print (average([0,0,3,1,4,1,5,9,0,0]))
print (average([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20]))


def average2(x):
    return sum(x)/float(len(x)) if x else 0
print(average2([0,0,3,1,4,1,5,9,0,0]))
print(average2([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20]))


def avg(data):
    if len(data)==0:
        return 0
    else:
        return sum(data)/float(len(data))
print(avg([0,0,3,1,4,1,5,9,0,0]))

from statistics import mean
print(mean([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20]))
print(mean([10**10000, -10**10000, 3, 1, 4, 1, 5, 9, 0, 0]))

