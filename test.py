import numpy
import wave

# 'rb' is binary reading modes. otherweise EOL chars corrupt on windows
wavefile = wave.open("tmp/11k16bitpcm.wav", 'rb')

channels = wavefile.getnchannels()
sampwidth = wavefile.getsampwidth()
nsamp = wavefile.getnframes()
framerate = wavefile.getframerate()
print ("channel, sampwidth, framerate, nframes, comptype, compname")
print wavefile.getparams()

length = float(nsamp)/float(framerate)
print "Length: " + str(length) + "s"

data = numpy.frombuffer(wavefile.readframes(nsamp), dtype="i" + str(sampwidth))
print "legnth of numpy array: " + str(data.shape)
print "here are a few samples"
print data[0]
print data[150000]
print data[21000]
print "mean"
print numpy.mean(data)
print numpy.max(data)
print numpy.min(data)