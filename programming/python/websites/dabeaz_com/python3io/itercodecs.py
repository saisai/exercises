# itercodecs.py
#
# Iterate over the lines of a file using codecs.open()

from timethis import timethis
import codecs

with timethis("Iterate over lines (codecs,latin-1)"):
    for line in codecs.open("access-log",encoding="latin-1"):
        pass

with timethis("Iterate over lines (native open)"):
    for line in open("access-log"):
        pass
