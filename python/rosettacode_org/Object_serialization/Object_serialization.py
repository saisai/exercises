# Object Serialization in Python
# serialization in python is accomplished via the Pickle module.
# Alternatively, one can use the cPickle module if speed is the key,
# everything else in this example remains the same.

import pickle

class Entity:
    def __init__(self):
        self.name = 'Entity'

    def printName(self):
        print(self.name)

class Person(Entity): # OldMan inherits from Entity

    def __init__(self): # override constructor
        self.name = "Cletus"

instance1 = Person()
instance1.printName()

instance2 = Entity()
instance2.printName()

filename = "objects.dat"
print("Serialized...")
serialized = pickle.dumps((instance1, instance2))

with open(filename, 'wb') as fo:
    fo.write(serialized)

with open(filename, 'rb') as fo:
    raw_data = fo.read()

i1, i2 = pickle.loads(raw_data)

print('Unserilized...')
i1.printName()
i2.printName()

