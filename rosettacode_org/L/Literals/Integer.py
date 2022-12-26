# Bin(leading 0b or 0B), Oct(leading 0o or 0O), Dec, Hex(leading 0x or 0X), in order:
# Python 3.0 brought in the binary literal and uses 0o or 0O exclusively for octal.
t = 0b1011010111 == 0o1327 == 727 == 0x2d7
print(t)

# Python 2.6 has the binary and new octal formats of 3.0, as well as keeping the earlier leading 0 octal format of previous 2.X versions for compatability.
# Bin(leading 0b or 0B), Oct(leading 0o or 0O, or just 0), Dec, Hex(leading 0x or 0X), in order:
#c = 0b1011010111 == 0o1327 == 01327 == 727 == 0x2d7