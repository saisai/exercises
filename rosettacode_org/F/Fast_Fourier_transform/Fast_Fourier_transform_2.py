from numpy.fft import fft
from numpy import array
a = array([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])
print(" ".join("%5.3f" % abs(f) for f in fft(a)))
