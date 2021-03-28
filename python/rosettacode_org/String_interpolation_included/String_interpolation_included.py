original = 'Mary had a %s lamb.'
extra = 'little'
print(original % extra)


original_2 = 'Mary had a {extra} lamb.'
extra = 'little'
print(original_2.format(**locals()))


original_3 = 'Mary had a {0} lamb.'
extra = 'little'
print(original_3.format(extra))


from string import Template
original_4 = Template("Mary had a $extra lamb.")
extra = 'little'
print(original_4.substitute(**locals()))


extra = 'little'
print(f'Mary had a {extra} lamb.')
