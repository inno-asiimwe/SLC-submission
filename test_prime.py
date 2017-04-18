import unittest
from primes import primes

class PrimeNumberTest(unittest.TestCase):
    def setUp(self):
        self.primes = primes(100)

    def test_for_string_input(self):
        self.assertRaises(TypeError, primes.primes, 'two' )

    def test_for_float_input(self):
        self.assertRaises(TypeError, primes.primes, 4.9)

    def test_for_prime_in_output(self):
        b = primes(100)
        self.assertIn(7, b)

    def test_for_nonprime_in_output(self):
        b = primes(100)
        self.assertNotIn(9, b)

    def test_for_input_less_than_2(self):
        self.assertRaises(ValueError, primes.primes, 1)
