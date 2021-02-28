from sys import stdin, stdout

def fwd(c):
    if c.isalpha():
        return [stdout.write(c), (yield from fwd((yield f)))][1]
    else:
        return c

def rev(c):
    if c.isalpha():
        return [(yield from rev((yield r))), stdout.write(c)][0]
    else:
        return c


def fw():
    while True:
        stdout.write((yield from fwd((yield r))))


def re():
    while True:
        stdout.write((yield from rev((yield f))))


f = fw()
r = re()
next(f)
next(r)


coro = f

#t = "what,is,the;meaning,of:life."
t = "what is the meaning of life."
for c in t:        
    if not c:
        break
    coro = coro.send(c)

#echo "what,is,the;meaning,of:life." | python Odd_word_problem_2.py
#echo "we,are;not,in,kansas;any,more." | python Odd_word_problem_2.py

