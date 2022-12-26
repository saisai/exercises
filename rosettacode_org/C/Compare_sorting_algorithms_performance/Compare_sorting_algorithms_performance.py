def builtinsort(x):
    x.sort()


def partition(seq, pivot):
    low, middle, up = [], [], []
    for x in seq:
        if x < pivot:
            low.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            up.append(x)
    return low, middle, up


import random


def qsortranpart(seq):
    size = len(seq)
    if size < 2: return seq
    low, middle, up = partition(seq, random.choice(seq))
    return qsortranpart(low) + middle + qsortranpart(up)


def ones(n):
    return [1] * n


def reversedrange(n):
    return reversed(range(n))


def shuffledrange(n):
    x = range(n)
    random.shuffle(x)
    return x

def insertion_sort(L):
    for i, value in enumerate(L):
        for j in range(i - 1, -1, -1):
            if L[j] > value:
                L[j + 1] = L[j]
                L[j] = value

def qsort(L):
    return (qsort([y for y in L[1:] if y <  L[0]]) +
            L[:1] +
            qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L

def write_timings(npoints=10, maxN=10**4, sort_functions=(builtinsort,insertion_sort, qsort),
                  sequence_creators = (ones, range, shuffledrange)):
   Ns = range(2, maxN, maxN//npoints)
   for sort in sort_functions:
       for make_seq in sequence_creators:
           Ts = [usec(sort, (make_seq(n),)) for n in Ns]
           writedat('%s-%s-%d-%d.xy' % (sort.__name__,  make_seq.__name__, len(Ns), max(Ns)), Ns, Ts)

def writedat(filename, x, y, xprecision=3, yprecision=5):
    with open(filename,'w') as f:
        for a, b in zip(x, y):
            print("%.*g\t%.*g" % (xprecision, a, yprecision, b), file=f)
            #or, using the new-style formatting:
            #print("{1:.{0}g}\t{3:.{2}g}".format(xprecision, a, yprecision, b), file=f)

import sys, timeit
def usec(function, arguments):
    modname, funcname = __name__, function.__name__
    timer = timeit.Timer(stmt='%(funcname)s(*args)' % vars(),
                         setup='from %(modname)s import %(funcname)s; args=%(arguments)r' % vars())
    try:
        t, N = 0, 1
        while t < 0.2:
            t = min(timer.repeat(repeat=3, number=N))
            N *= 10
        microseconds = round(10000000 * t / N, 1) # per loop
        return microseconds
    except:
        timer.print_exc(file=sys.stderr)
        raise

import operator
import numpy, pylab
def plotdd(dictplotdict):
   """See ``plot_timings()`` below."""
   symbols = ('o', '^', 'v', '<', '>', 's', '+', 'x', 'D', 'd',
              '1', '2', '3', '4', 'h', 'H', 'p', '|', '_')
   colors = list('bgrcmyk') # split string on distinct characters
   for npoints, plotdict in dictplotdict.iteritems():
       for ttle, lst in plotdict.iteritems():
           pylab.hold(False)
           for i, (label, polynom, x, y) in enumerate(sorted(lst,key=operator.itemgetter(0))):
               pylab.plot(x, y, colors[i % len(colors)] + symbols[i % len(symbols)], label='%s %s' % (polynom, label))
               pylab.hold(True)
               y = numpy.polyval(polynom, x)
               pylab.plot(x, y, colors[i % len(colors)], label= '_nolegend_')
           pylab.legend(loc='upper left')
           pylab.xlabel(polynom.variable)
           pylab.ylabel('log2( time in microseconds )')
           pylab.title(ttle, verticalalignment='bottom')
           figname = '_%(npoints)03d%(ttle)s' % vars()
           pylab.savefig(figname+'.png')
           pylab.savefig(figname+'.pdf')
           print(figname)

import collections, itertools, glob, re
import numpy
def plot_timings():
   makedict = lambda: collections.defaultdict(lambda: collections.defaultdict(list))
   df = makedict()
   ds = makedict()
   # populate plot dictionaries
   for filename in glob.glob('*.xy'):
       m = re.match(r'([^-]+)-([^-]+)-(\d+)-(\d+)\.xy', filename)
       print(filename)
       assert m, filename
       funcname, seqname, npoints, maxN = m.groups()
       npoints, maxN = int(npoints), int(maxN)
       a = numpy.fromiter(itertools.imap(float, open(filename).read().split()), dtype='f')
       Ns = a[::2]  # sequences lengths
       Ts = a[1::2] # corresponding times
       assert len(Ns) == len(Ts) == npoints
       assert max(Ns) <= maxN
       #
       logsafe = numpy.logical_and(Ns>0, Ts>0)
       Ts = numpy.log2(Ts[logsafe])
       Ns = numpy.log2(Ns[logsafe])
       coeffs = numpy.polyfit(Ns, Ts, deg=1)
       poly = numpy.poly1d(coeffs, variable='log2(N)')
       #
       df[npoints][funcname].append((seqname, poly, Ns, Ts))
       ds[npoints][seqname].append((funcname, poly, Ns, Ts))
   # actual plotting
   plotdd(df)
   plotdd(ds) # see ``plotdd()`` above

sort_functions = [
    builtinsort,         # see implementation above
    insertion_sort,      # see [[Insertion sort]]
    #insertion_sort_lowb, # ''insertion_sort'', where sequential search is replaced
                         #     by lower_bound() function
    qsort,               # see [[Quicksort]]
    #qsortranlc,          # ''qsort'' with randomly choosen ''pivot''
                         #     and the filtering via list comprehension
    qsortranpart,        # ''qsortranlc'' with filtering via ''partition'' function
    #qsortranpartis,      # ''qsortranpart'', where for a small input sequence lengths
    ]                    #     ''insertion_sort'' is called
if __name__=="__main__":
   import sys
   sys.setrecursionlimit(10000)
   write_timings(npoints=100, maxN=1024, # 1 <= N <= 2**10 an input sequence length
                 sort_functions=sort_functions,
                 sequence_creators = (ones, range, shuffledrange))
   plot_timings()