from __future__ import print_function
from multiprocessing import Pool

def main():
    p = Pool()
    p.map(print, "Enjoy Roseeta Code".split())

if __name__ == '__main__':
    main()
