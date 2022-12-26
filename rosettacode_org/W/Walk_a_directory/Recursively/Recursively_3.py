from fnmatch import fnmatch
import os, os
 
def print_fnmatches(pattern, dir, files):
    for filename in files:
        if fnmatch(filename, pattern):
            print(os.path.join(dir, filename))
 
os.walk('/', print_fnmatches, '*.py')