
from random import randint

def do_scan(mat):
    for row in mat:
        for item in row:
            print(item)
            if item == 20:
                print()
                return
        print()
    print()

mat = [[randint(1, 20) for x in range(10)] for y in range(10)]
print(list(mat))
do_scan(mat)
