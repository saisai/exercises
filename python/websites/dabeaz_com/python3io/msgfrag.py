# msgfrag.py
#
# Three different techniques of forming a large message from fragments of bytes.

from timethis import timethis

FRAGMENT_SIZE = 256
NUMBER_FRAGS  = 10000

# A generator that creates byte fragments for us
def make_fragments(size,count):
    frag = b"x"*size
    while count > 0:
        yield frag
        count -= 1

# Try byte concatenation
with timethis("Byte concatenation +="):
    msg = b""
    for chunk in make_fragments(FRAGMENT_SIZE, NUMBER_FRAGS):
        msg += chunk

# Try .join()
with timethis("Joining a list of fragments"):
    msgparts = []
    for chunk in make_fragments(FRAGMENT_SIZE, NUMBER_FRAGS):
        msgparts.append(chunk)
    msg = b"".join(msgparts)

# Try bytearray.extend
with timethis("Extending a bytearray"):
    msg = bytearray()
    for chunk in make_fragments(FRAGMENT_SIZE, NUMBER_FRAGS):
        msg.extend(chunk)



