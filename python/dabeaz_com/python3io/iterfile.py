# iterfile.py
#
# Iterate over the lines of a file using native open()

from timethis import timethis

with timethis("Iterate over lines"):
    for line in open("access-log"):
        pass
