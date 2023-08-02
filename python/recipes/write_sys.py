import sys
with open('sys.txt', 'w') as f:
   for i in dir(sys):
       f.write(i)
       f.write(' => ')
       f.write(str(getattr(sys, i)))
       f.write('\n')
