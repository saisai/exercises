# iterenc.py
#
# Iterate over the lines of a file using three different encodings

from timethis import timethis
import codecs

with timethis("Iterate over lines (UTF-8)"):
    for line in open("access-log",encoding='utf-8'):
        pass

with timethis("Iterate over lines (ASCII)"):
    for line in open("access-log",encoding='ascii'):
        pass

with timethis("Iterate over lines (Latin-1)"):
    for line in open("access-log",encoding='latin-1'):
        pass
