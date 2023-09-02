import numpy as np
import multiprocessing as mp
path = 'C:\\Users\\sys\\PycharmProjects\\MPtest\\*.gwf'
filenames = [os.path.basename(x) for x in glob.glob(path)]
filelist= sorted(filenames, key=lambda x: float(re.findall("(\d+)", x)[0]))
channelslist = ["VALUE_" + str(int(n)) for n in np.linspace(201, 234, 34)]
rows = 500000
cols = len(channelslist)  # No. of channels involved in the measurement

def myfunc(filename_arg):
    sensdataarray = np.zeros((rows, cols))
    for inumber, iname in enumerate(channelslist):
        sensdataarray[:, inumber] = framel.frgetvect(filename_arg, iname, verbose=False)[0]
    return sensdataarray

# MP
print("no of CPUs:", mp.cpu_count())
if __name__ == '__main__':
  pool = mp.Pool()

  my_result = pool.map(myfunc, filelist) 
# when 'filelist' contain single element then 'my_result' gives the value of 'np_array_list' 
#but when 'filelist' contains multiple element then 'my_result' does not give any result!!
  pool.close()
  pool.join()
  print('My result is :', my_result)
  
'''
import glob
import os
import re

import framel
import parmap
import numpy as np

def myfunc(filename_arg, rows, channelslist):
    cols = len(channelslist)
    sensdataarray = np.zeros((rows, cols))
    for inumber, iname in enumerate(channelslist):
        sensdataarray[:, inumber] = framel.frgetvect(filename_arg, iname, verbose=False)[0]
    return sensdataarray


if __name__ == '__main__':
    path = 'C:\\Users\\sys\\PycharmProjects\\MPtest\\*.gwf'
    filenames = [os.path.basename(x) for x in glob.glob(path)]
    filelist= sorted(filenames, key=lambda x: float(re.findall("(\d+)", x)[0]))
    channelslist = ["VALUE_" + str(int(n)) for n in np.linspace(201, 234, 34)]
    my_result = parmap.map(myfunc, filelist, rows=500000, channelslist=channelslist)
    print('My result is :', my_result)
'''

# https://stackoverflow.com/questions/69423498/python-multiprocessing-while-listing-the-files-and-extract-data-from-list