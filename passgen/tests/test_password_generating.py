import unittest
import re
from passgen import Password

class TestGenerators(unittest.TestCase):
    def test_minimum(self):
        # Check if minimum numbers works
        self.assertGreaterEqual(len(re.findall("[0-9]", Password(32,False,5,0).generate())), 5)
        # Check if minimum symbols works
        self.assertGreaterEqual(len(re.findall("[!@#$%^&*]", Password(32,False,0,5).generate())), 5)
        with self.assertRaises(ValueError):
            # Check if alphanumeric throws a ValueError with minimum_symbols>0
            Password(64,True,0,1).generate()
            # Check if exceeding minimum numbers throws an error
            Password(12,False,13,0).generate()
            # Check if exceeding minimum symbols throws an error
            Password(12,False,0,13).generate()
            # Check if exceeding minimums throw an error
            Password(12,False,6,7).generate()


    def test_xkcd(self):
        # Check for additional dashes
        self.assertEqual(Password(4).generate_xkcd().count('-'), 3)
        # Check if amount of words is correct.
        self.assertEqual(len(Password(9).generate_xkcd().split('-')), 9)
        # Check if xkcd blocks greater amount of words than 10
        with self.assertRaises(ValueError): 
            Password(11).generate_xkcd()
if __name__ == "__main__":
    unittest.main()
