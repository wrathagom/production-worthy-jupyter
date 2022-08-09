import unittest
import sys
from datetime import datetime as dt

# setting path
sys.path.append('../')

from functions import custom

class CustomFunctionTests(unittest.TestCase):

    def test_custom_strftime(self):
        result = custom.custom_strftime('%B {S}, %Y', dt.now())
        self.assertEqual(result, "August 9th, 2022")
    
    def test_suffix_st(self):
        result = custom.suffix(1)
        self.assertEqual(result, "st")
        
    def test_suffix_nd(self):
        result = custom.suffix(2)
        self.assertEqual(result, "nd")
        
    def test_suffix_rd(self):
        result = custom.suffix(3)
        self.assertEqual(result, "rd")
        
    def test_suffix_th(self):
        result = custom.suffix(31)
        self.assertEqual(result, "st")
    
# run the test
unittest.main()