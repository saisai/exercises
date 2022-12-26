
import collections
import re

count = 10

with open('../unixdict.txt') as f:
    text = f.read()

word_freq = sorted(
    collections.Counter(sorted(re.split(r"\W+", text.lower()))).items(),
    key=lambda c: c[1],
    reverse=True,
)
 
for i in range(len(word_freq)):
    print("[{:2d}] {:>10} : {}".format(i + 1, word_freq[i][0], word_freq[i][1]))
    if i == count - 1:
        break
