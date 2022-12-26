from collections import Counter
from re import findall
import sys

def _count_words(fname):
    with open(fname) as f:
        text = f.read()
    print(type(text))
    words = findall(r'\w+', text.lower())
    return Counter(words)

def most_commom_words_in_file(fname, n):
    counts = _count_words(fname)
    for word, count in [['WORD', 'COUNT']] + counts.most_common(n):
        print(f'{word:>10} {count:>6}')

if __name__ == '__main__':
    fname = sys.argv[1]
    n = sys.argv[2]
    most_commom_words_in_file(fname, int(n))
    
    
    # python Word_frequency_2.py ../unixdict.txt 10
