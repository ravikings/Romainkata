import unittest
from romain_converter import *

class TestStringMethods(unittest.TestCase):
    # Test for output is correct
    def test_1(self):
        self.assertEqual(intToRoman(200), 'CC')
    
    def test_2(self):
        self.assertEqual(intToRoman(1), 'II')

    def test_2(self):
        self.assertEqual(intToRoman(10), 'II')

    def test_2(self):
        self.assertEqual(intToRoman(1000), 'II')

    #here is test for one failure and one passing
    def test_2(self):
        self.assertEqual(intToRoman(1500), 'MD')
        self.assertFalse(intToRoman(1500), 'ii')

if __name__ == '__main__':
    unittest.main()