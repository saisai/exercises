

import numpy as np

np_array = np.array([1,2,3,4,5])
print('Contents of the ndArray :')
print(np_array)

# create numpy array from a tuple
np_tuple = np.array((1,2,3,4,5))
print(np_tuple)

print(type(np_tuple))
print(np_tuple.dtype)


# create 2d numpy array from a list of list

np_2d = np.array([[77, 88, 99] , [31,42,63] , [11,22,33]])
print(np_2d)

# Create 1D Numpy Array from list of list
listOfLists = [[77, 88, 99], [31, 42, 63], [11, 22, 33]]

np_1d = np.array([elem for singleList in listOfLists for elem in singleList])

print(np_1d)


# Create a Numpy Array from a list with different data type

np_diff = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9] , dtype=float)
print(np_diff )



