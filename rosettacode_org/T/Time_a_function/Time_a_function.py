
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

from math import pow
def nothing(): pass
def identity(x): return x


def qsort(L):
    print(L)
    return (qsort([y for y in L[1:] if y <  L[0]]) +
            L[:1] +
            qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L

def qsort(list):
    print(list)
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

#print(usec(nothing, []))
#print(usec(identity, [1]))
#print(usec(pow, (2, 100)))
#print([usec(qsort, (list(range(n)),)) for n in range(10)])
print([usec(quickSort, (list(range(n)),)) for n in range(10)])

