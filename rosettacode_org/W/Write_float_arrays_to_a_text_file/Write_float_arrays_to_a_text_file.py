"""
Write float arrays to a text file

Task
Write two equal-sized numerical arrays 'x' and 'y' to a two-column text file named 'filename'.

The first column of the file contains values from an 'x'-array with a given 'xprecision', the second -- values from 'y'-array with 'yprecision'.

For example, considering:

 x = {1, 2, 3, 1e11};
   y = {1, 1.4142135623730951, 1.7320508075688772, 316227.76601683791};
                                                          /* sqrt(x) */
   xprecision = 3;
   yprecision = 5;
   The file should look like:

   1    1
   2    1.4142
   3    1.7321
   1e+011   3.1623e+005
"""
def writedat(filename, x, y, xprecision=3, yprecision=5):
    with open(filename, 'w') as f:
        for a, b in zip(x, y):
            print("%.*g\t%.*g" %(xprecision, a, yprecision, b), file=f)
            #or, using the new-style formatting:
            #print("{1:.{0}g}\t{3:.{2}g}".format(xprecision, a, yprecision, b), file=f)

import math
x = [1, 2, 3, 1e11]
y = map(math.sqrt, x)
print(y)
writedat('sqrt.data', x, y)

for line in open('sqrt.data'):
    print(line)
