import numpy
import time
x=numpy.random.random(10000)
t0=time.time()
for i in numpy.arange(1000):
        numpy.fft.fft(x)

print "took %f" % (time.time()-t0)
x=numpy.random.random(4*2048)
t0=time.time()
for i in numpy.arange(1000):
        numpy.fft.fft(x)

print "took %f" % (time.time()-t0)
