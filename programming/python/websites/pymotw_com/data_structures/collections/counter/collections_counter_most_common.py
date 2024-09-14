import collections

c = collections.Counter()
with open('collections_counter_most_common.py', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())


print('More common:')
for letter, count in c.most_common(3):
    print('{} : {:>7}'.format(letter, count))

