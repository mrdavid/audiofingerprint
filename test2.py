from fingerprinter.wrapper.Fingerprinter import Fingerprinter
import pylab
import numpy

#test = fingerprinter.Fingerprinter(filepath="tmp/11k16bitpcm.wav")
#test = fingerprinter.Fingerprinter(filepath="tmp/440Hz_44100Hz_16bit_30sec.wav", framewidth=0.37)
#test.init_fingerprints()

#test3 = fingerprinter.Fingerprinter(filepath="tmp/from_min_01_09TheSuffering.wav", framewidth=0.37, overlap=0.1)
#test3.init_fingerprints()

print "done"

test2 = Fingerprinter(filepath="tmp/11k16bitpcm.wav", framewidth=0.37, overlap=0.1)
test2.init_fingerprints()
test2.print_info()


#print test2.binary_distance([True, True, True], [False, True, False])

#print test2.block_distance(numpy.array([[True, True, True], [True, True, True]]), numpy.array([[False, True, False], [False, True, True]]))


#test.print_info()
#print test.frequency_band_boundary_indices
#print test.fingerprints_binary[0]

print "Calculated fingerprints now finding"
#test2.find_position(test3)

#pylab.figure()
#pylab.subplot(121)
#pylab.imshow(test3.fingerprints_binary[256:2*256])
#pylab.subplot(122)
#pylab.imshow(test2.fingerprints_binary[256:2*256])
#pylab.subplot(123)
#pylab.imshow(test3.fingerprints_binary[256:2*256])
#pylab.show()
