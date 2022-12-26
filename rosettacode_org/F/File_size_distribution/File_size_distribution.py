import sys, os
from collections import Counter

def dodir(path):
    global h

    for name in os.listdir(path):
        p = os.path.join(path, name)

        if os.path.islink(p):
            pass
        elif os.path.isfile(p):
            h[os.stat(p).st_size] += 1
        elif os.path.isdir(p):
            dodir(p)
        else:
            pass
        #print('h', h)
        
def main_test(arg):
    global h
    h = Counter()
    for dir in arg:
        dodir(dir)

def main(arg):
    global h
    h = Counter()
    print('h ', h)
    for dir in arg:
        dodir(dir)

    s = n = 0
    for k, v in sorted(h.items()):
        print("Size %d -> %d file(s)" % (k, v))

        n += v
        s += k * v
    print('Total %d bytes for %d files' % (s, n))



if __name__ == '__main__':
    main(sys.argv[1:])


