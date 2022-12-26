hash = dict()  # 'dict' is the dictionary type.
hash = dict(red="FF0000", green="00FF00", blue="0000FF")
hash = { 'key1':1, 'key2':2, }
#value = hash[key]

# empty dictionary
d = {}
d['spam'] = 1
d['eggs'] = 2

# dictionaries with two keys
d1 = {'spam': 1, 'eggs': 2}
d2 = dict(spam=1, eggs=2)

# dictionaries from tuple list
d1 = dict([('spam', 1), ('eggs', 2)])
d2 = dict(zip(['spam', 'eggs'], [1, 2]))

# iterating over keys
for key in d:
    print(key, d[key])

# iterating over (key, value) pairs
for key, value in d.items():
    print(key, value)