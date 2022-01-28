class Hashable:

    def __hash__(self):
        return id(self) ^ 0xBEEF


my_inst = Hashable()
print(my_inst)
my_int = 1
my_complex = 0 + 1j
my_float = 1.2
my_string = "Spam"
my_bool = True
my_unicode = u'Ham'
my_list = ['a', 7]
my_tuple = ( 0.0, 1.4 )
my_set = set(my_list)

def my_func():
    pass

class my_class:
    pass

keys = [my_inst, my_tuple, my_int, my_complex, my_float, my_string,
	my_bool, my_unicode, frozenset(my_set), tuple(my_list),
	my_func, my_class]

values = range(12)
d = dict(zip(keys, values))
for key, value in d.items():
    print(key, ':', value)




keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {key: value for key, value in zip(keys, values)}
print('hash', hash)

