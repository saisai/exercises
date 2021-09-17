
for i in range(16): print('{0:b}'.format(i))

for i in range(16): print(bin(i)[2:])
print()
oct2bin = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
bin = lambda n: ''.join(oct2bin[octdigit] for octdigit in '%o' % n).lstrip('0') or '0'
for i in range(16): print(bin(i))

