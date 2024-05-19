import unittest
import passgen

class TestEntropy(unittest.TestCase):
    def test_calculate_entropy(self):
        self.assertEqual(passgen.Entropy("Chipi12Chapa").calculate(), 71.45) # Only Alphanumeric
        self.assertEqual(passgen.Entropy("Password12!").calculate(), 67.42) # Alphanumeric + Symbols
        self.assertEqual(passgen.Entropy(passgen.Password(64,False,0,0).generate()).calculate(), 392.27)

        # TODO: Write tests for xkcd entropy.

if __name__ == "__main__":
    unittest.main()
