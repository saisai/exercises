import numpy as np


arr = np.zeros(5)
print(arr)

arr2 = np.zeros(5, dtype=np.int64)
print(arr2)


arr_2d = np.zeros((4, 5), dtype=np.int64)
print(arr_2d)



arr_3d = np.zeros((2,4,5), dtype=np.int64)
print(arr_3d)

print('4 d')
arr_4d = np.zeros((3,2,4,5),dtype=np.int64)
print(arr_4d)

