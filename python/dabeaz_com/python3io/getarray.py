# getarray.py
#
# Receive a large binary array over a pipe using readinto

import sys
import array

# Preallocate the array
a = array.array("I",[0])*10000000

# Read it.  Note: buffer is the binary mode file underlying the text stream
sys.stdin.buffer.readinto(a)

# Verify the contents
for n in range(10000000):
    if a[n] != n:
        print("Fail : {:d}".format(n))
        break
else:
    print("Passed")