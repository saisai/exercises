"""
# Instead of this
self.release_water()
self.shutdown()
self.alarm()

class Reactor:
    ...
    def release_water(self):
        self.valve.open()
        return self

self.release_water().shutdown().alarm()   

Instead of writing methods without return values, make them return self
allows cascading of methods
https://stevenloria.com/python-best-practice/
https://stevenloria.com/archives
https://gist.github.com/highsmallxu/4bea7487bca93b1aacf8f0f261923797#file-lazy_evaluation_class_properties-py
"""

class Reactor:
    def release_water(self):
        print('release_water')
        return self

    def shutdown(self):
        print('shutdown')
        return self

    def alarm(self):
        print('alarm')
        return self

r = Reactor()
r.release_water().shutdown().alarm()
