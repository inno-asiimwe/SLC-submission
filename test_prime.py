import unittest
from primes import primes

class PrimeNumberTest(unittest.TestCase):
    def setUp(self):
        self.primes = primes()

    def test_for_string_input(self):
        self.assertRaises(ValueError, self.primes, 'two')

    def test_for_float_input(self):
        self.assertRaises(ValueError, self.primes, 4.9)

    def test_for_prime_in_output(self):
        b = primes(100)
        self.assertIn(7, b)

    def test_for_nonprime_in_output(self):
        b = primes(100)
        self.assertNotIn(9, b)

    