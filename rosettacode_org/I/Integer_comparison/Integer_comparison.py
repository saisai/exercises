import sys

try:
    a = input("Enter value of a: ")
    b = input("Enter value of b: ")
except (ValueError, EnvironmentError) as err:
    print(sys.stderr, "Erroneuous input: ", err)
    sys.exit(1)

def cmp(a, b):
    return (a > b) - (a < b)

dispatch = {
    -1: 'is less than',
     0: 'is equal to',
     1: 'is greater than'
     }
print(a, dispatch[cmp(a, b)], b)



