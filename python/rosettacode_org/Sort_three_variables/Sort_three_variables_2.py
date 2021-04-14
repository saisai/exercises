#python2 Code for Sorting 3 values
a= input("Enter values one by one ..\n1.").strip()
b=input("2.").strip()
c=input("3.").strip()
if a>b :
   a,b = b,a
if a>c:
   a,c = c,a
if b>c:
   b,c = c,b
print(str(a)+" "+str(b)+" "+str(c))