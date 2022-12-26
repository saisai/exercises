
from itertools import cycle, count, islice

fizzes = cycle([""] * 2 + ["Fizz"])
buzzes = cycle([""] * 4 + ["Buzz"])
both = (f + b for f , b in zip(fizzes, buzzes))

# if the string is "", yield the number
# otherwise yield the string
fizzbuzz = (word or n for word, n in zip(both, count(1)))

# print the first 100
for i in islice(fizzbuzz, 100):
    print(i)
