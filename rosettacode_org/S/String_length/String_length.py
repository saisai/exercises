# -*- coding: UTF-8 -*-

print(len(b"Hello, world!"))

# The letter Alef
print(len('\u05d0'.encode())) # the default encoding is utf-8 in Python3
# 2
print(len('\u05d0'.encode('iso-8859-8')))
# 1

s = "møøse"
assert len(s) == 5
assert len(s.encode('UTF-8')) == 7
assert len(s.encode('UTF-16-BE')) == 10 # There are 3 different UTF-16 encodings: LE and BE are little endian and big endian respectively, the third one (without suffix) adds 2 extra leading bytes: the byte-order mark (BOM).
u="𝔘𝔫𝔦𝔠𝔬𝔡𝔢"
assert len(u.encode()) == 28
assert len(u.encode('UTF-16-BE')) == 28

print(len("𝔘𝔫𝔦𝔠𝔬𝔡𝔢"))

import sys
sys.maxunicode # 1114111 on a wide build, 65535 on a narrow build
print(sys.maxunicode)

print(len('ascii'))
# 5
print(len('\u05d0')) # the letter Alef as unicode literal
# 1
print(len(b'\xd7\x90'.decode('utf-8'))) # Alef encoded as utf-8 byte sequence
# 1

print(hex(sys.maxunicode), len(chr(0x1F4A9)))
# ('0x10ffff', 1)

print(hex(sys.maxunicode), len(chr(0x1F4A9)))