
# Callable class

class Fiblike():
    def __init__(self, start):
        self.addnum = len(start)
        self.memo = start[:]

    def __call__(self, n):
        try:
            return self.memo[n]
        except IndexError:
            ans = sum(self(i) for i in range(n-self.addnum, n))
            self.memo.append(ans)
            return ans

fibo = Fiblike([1,1])
print([fibo(i) for i in range(10)])

lucas = Fiblike([2,1])
print([lucas(i) for i in range(10)])

for n, name in zip(range(2,11), 'fibo tribo tetra penta hexa hepta octo nona deca'.split()) :
	fibber = Fiblike([1] + [2**i for i in range(n-1)])
	print('n=%2i, %5snacci -> %s ...' % (n, name, ' '.join(str(fibber(i)) for i in range(15))))
