from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print(sorted(d.items()))

# https://docs.python.org/3.5/library/collections.html#defaultdict-examples

dd = {}
for k, v in s:
    dd.setdefault(k, []).append(v)

print(sorted(dd.items()))


s = 'mississippi'

ss = defaultdict(int)
for k in s:
    ss[k] += 1

print(sorted(ss.items()))

def constant_factory(value):
    return lambda: value

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

print(sorted(d.items()))