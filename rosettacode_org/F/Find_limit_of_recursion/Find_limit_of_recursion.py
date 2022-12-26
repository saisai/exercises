
import sys


def set_recursion_limit():
    
    sys.setrecursionlimit(12345)

def defaut_recursion_limit():
    print(sys.getrecursionlimit())


def recurse(counter):
    print(counter)
    counter += 1
    recurse(counter)


#print(recurse(1))

def recurseDeeper(counter):
    try:
        print(counter)
        recurseDeeper(counter + 1)
    except RecursionError:
        print("RecursionError at depth", counter)
        recurseDeeper(counter + 1)

recurseDeeper(1)


