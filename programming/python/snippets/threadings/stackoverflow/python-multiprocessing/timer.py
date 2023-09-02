import threading


class Struct:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

res = {'is_busy': True}
s = Struct(**res)

from threading import Timer

class CustomTimer(Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomTimer, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
       self.result = self._original_function(*a, **kw)

    def join(self):
        super(CustomTimer, self).join()
        return self.result

def add_together(a, b):
    return a + b

def free_up_client(client):
    client.is_busy = False
    return client

#c = CustomTimer(1, add_together, (2, 4))
c = CustomTimer(5, free_up_client, [s])
c.start()
print(c.join())
a = c.join()
print(dir(a))
print(a.is_busy)
'''
def free_up_client(client):
    client.is_busy = False

if __name__== '__man__':
    timer = threading.Timer(30, free_up_client, s)
    print(s.is_busy)
    print(timer.kwargs)
    print(dir(timer))
'''

# https://stackoverflow.com/questions/28635985/extending-threading-timer-for-returning-value-from-function-gives-typeerror