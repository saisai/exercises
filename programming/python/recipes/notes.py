class X(object):

	def __len__(self):
		return 1 << 31
        

print(len(X())

# 32-bit
MAXSIZE = int((1 << 31) - 1)

# 64-bit
MAXSIZE = int((1 << 63) - 1)


"""
Providing iterator functions that are not in all version of Python we support.
Where possible, we try to use the system-native version and only fall back to
these implementations if necessary.
"""


def is_iterable(x):
    "A implementation independent way of checking for iterables"
    try:
        iter(x)
    except TypeError:
        return False
    else:
        return True


# https://en.wikipedia.org/wiki/Primitive_data_type
# https://diveinto.org/python3/native-datatypes.html
# https://github.com/mantidproject/mantid/tree/master/scripts/Calibration
# https://www.mantidproject.org/Basic_PythonAlgorithm_Structure
# https://www.python.org/dev/peps/pep-0232/
# https://www.electronics-tutorials.ws/accircuits/ac-waveform.html
# https://www.electronics-notes.com/articles/basic_concepts/
# https://www.instructables.com/Basic-Electronics/
# https://stackoverflow.com/questions/104983/what-is-thread-local-storage-in-python-and-why-do-i-need-it
# https://pythontic.com/multithreading/synchronization/thread-local-storage
# https://www.bogotobogo.com/python/Multithread/python_multithreading_Thread_Local_Specific_Data.php

from time import sleep
from random import random
from threading import Thread, local

data = local()

def bar():
    print("I'm called from", data.v)

def foo():
    bar()

class T(Thread):
    def run(self):
        sleep(random())
        data.v = self.getName()   # Thread-1 and Thread-2 accordingly
        sleep(1)
        foo()
        
# T().start(); T().start()        


from time import sleep
from random import random
from threading import Thread

def bar():
    global v
    print("I'm called from", v)

def foo():
    bar()

class T(Thread):
    def run(self):
        global v
        sleep(random())
        v = self.getName()   # Thread-1 and Thread-2 accordingly
        sleep(1)
        foo()
        
#T().start(); T().start()        