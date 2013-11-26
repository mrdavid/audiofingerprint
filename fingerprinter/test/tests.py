import imp
import unittest
import numpy.testing as ntest
from .. import wrapper as fingerprinter

class FrequencyBandsTest(unittest.TestCase):
  def testCalculate(self):
    f = fingerprinter.Fingerprinter(filepath="fingerprinter/test/data/11k16bitpcm.wav", framewidth=0.37, overlap=0.1)
    try:
      ntest.assert_array_equal(f.calculate_frequency_bands(4079, 0.37), [111,117,124,131,139,147,156,165,175,186,197,208,221,234,248,262,278,294,312,330,350,371,393,416,441,467,494,524,555,587,622,659,698,740])
    except AssertionError:
      self.fail("Frequency bands are not being calculated correctly.")
    
    
if __name__ == "__main__":
  unittest.main()