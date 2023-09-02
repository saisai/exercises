import sys
'''
for l in sys.stdin:
    print("got: %s" % l)
'''
for line in iter(sys.stdin.readline, ''):
    print("got: %s" % line)
    sys.stdout.flush()