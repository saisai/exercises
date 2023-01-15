# iterbin.py
#
# Iterate over the lines of a file using binary mode

from timethis import timethis

with timethis("Iterate over lines (binary mode)"):
    for line in open("access-log","rb"):
        pass

with timethis("Iterate over lines (unbuffered binary mode)"):
    for line in open("access-log","rb",buffering=0):
        pass