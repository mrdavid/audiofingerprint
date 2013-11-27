import unittest
import numpy.testing as ntest

import math

from .. import wrapper as fingerprinter

filename = "fingerprinter/test/data/11k16bitpcm.wav"

# The wrapper class
class calculate_frequency_bands_test(unittest.TestCase):
  
  # Test the length of the frequency band boundary array. Should 
  # be the number of bits/fingerprint + 2
  def test_different_bitsizes(self):
    f = fingerprinter.Fingerprinter(filepath=filename, framewidth=0.37, overlap=0.1)
    
    for x in range(1, 33):
      f.FINGERPRINT_NBITS = x
      self.assertEqual((f.FINGERPRINT_NBITS + 2,), f.calculate_frequency_bands(4097, 0.37).shape)
    
    f.close()

  # The lowest and highest index only depend on the lowest and highest frequency
  # and the number of seconds/frame. they should be independent of the number of bits/sub-fingerprint
  def test_low_high_indices(self):
    # try out these different settings
    fw = [0.37, 0.5, 0.37, 0.5] # framewidth
    sp = [4097, 4097, 5000, 5000] # number of samples per frame
    fl = [300.0, 300.0, 200.0, 200.0] # lower frequency limit
    fh = [2000.0, 2000.0, 3000.0, 3000.0] # higher frequency limit
  
    for x in range(0, len(fw)):
      f = fingerprinter.Fingerprinter(filepath=filename, framewidth=fw[x], overlap=0.1)
      # set this before looping through the number of bits / fingerprint
      f.FREQUENCY_BAND_LOWER_LIMIT = fl[x]
      f.FREQUENCY_BAND_UPPER_LIMIT = fh[x]
    
      lower_index_should_be = float( math.floor( fl[x] * fw[x] ) )
      upper_index_should_be = float( math.ceil( fh[x] * fw[x] ) )
      for y in range(1, 33):
        f.FINGERPRINT_NBITS = y
        self.assertEqual(lower_index_should_be, f.calculate_frequency_bands(sp[x], fw[x])[0])
        self.assertEqual(upper_index_should_be, f.calculate_frequency_bands(sp[x], fw[x])[f.FINGERPRINT_NBITS + 1])
        
      f.close()
    
    
  
  # Just some random value compared with what the function outputs
  def test_default(self):
    f = fingerprinter.Fingerprinter(filepath=filename, framewidth=0.37, overlap=0.1)
    try:
      ntest.assert_array_equal(f.calculate_frequency_bands(4079, 0.37), [111,118,125,132,140,148,157,166,176,186,197,209,221,234,248,263,278,295,312,331,350,371,393,416,441,467,495,524,555,588,623,660,699,740])
    except AssertionError:
      self.fail("Frequency bands are not being calculated correctly.")


if __name__ == "__main__":
  unittest.main()