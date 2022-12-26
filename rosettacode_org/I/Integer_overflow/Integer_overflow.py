
for calc in '''   -(-2147483647-1)
   2000000000 + 2000000000
   -2147483647 - 2147483647
   46341 * 46341
   (-2147483647-1) / -1'''.split('\n'):
	ans = eval(calc)
	print('Expression: %r evaluates to %s of type %s'
	      % (calc.strip(), ans, type(ans)))
