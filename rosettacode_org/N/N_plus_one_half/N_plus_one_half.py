"""
http://rosettacode.org/wiki/Loops/N_plus_one_half
"""


print(', '.join(str(i+1) for i in range(10)))


from sys import stdout
write = stdout.write
n, i = 10, 1
while True:
    write(str(i))
    i += 1
    if i > n:
        break
    write(', ')
