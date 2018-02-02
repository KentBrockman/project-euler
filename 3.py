import unittest
import logging
import math


log = logging.getLogger('debug')


# this is way too slow to make work
def generate_primes(maximum):
    """Generate list of primes up to maximum"""
    primes = [2]
    for x in range(3, maximum + 1):
        # the idea here - only things that are divisible by 2, 3 and any other primes are ruled out.  is this right?
        if all([x % prime for prime in primes]):
            primes.append(x)
    return primes


def get_prime_factors(number):
    # TODO: change this strategy - generate factors first, inpsect for primes afterwards...
    prime_factors = []
    primes = generate_primes(number)

    for prime in primes:
        if number % prime is 0:
            prime_factors.append(prime)

    return prime_factors


def generate_factors(number):
    factors = []
    for x in range(1, int(math.sqrt(number))):
        if number % x is 0:
            factors.append(x)
            factors.append(number / x)
    return factors


def prime_check(number):
    # http://planetmath.org/howtofindwhetheragivennumberisprimeornot
    newnum = int(math.ceil(math.sqrt(number)))
    primes = generate_primes(newnum)
    return all([number % prime != 0 for prime in primes])


if __name__ == '__main__':
    prime_factors = generate_primes(int(math.sqrt(600851475143)))
    # prime_factors = get_prime_factors(600851475143)
    print(prime_factors)


class Test(unittest.TestCase):
    def test_generate_primes_15(self):
        primes = generate_primes(15)
        self.assertIn(2, primes)
        self.assertIn(3, primes)
        self.assertIn(5, primes)
        self.assertIn(7, primes)
        self.assertIn(11, primes)
        self.assertIn(13, primes)
        self.assertEqual(len(primes), 6)

    def test_generate_primes_30(self):
        primes = generate_primes(30)
        self.assertNotIn(25, primes)
        self.assertIn(29, primes)

    def test_generate_factors_10(self):
        factors = generate_factors(10)
        self.assertIn(1, factors)
        self.assertIn(2, factors)
        self.assertIn(5, factors)
        self.assertIn(10, factors)

    def test_main(self):
        prime_factors = get_prime_factors(13195)
        self.assertIn(5, prime_factors)
        self.assertIn(7, prime_factors)
        self.assertIn(13, prime_factors)
        self.assertIn(29, prime_factors)

    def test_prime_check(self):
        self.assertFalse(prime_check(4), '4 shouldnt be prime')
        self.assertTrue(prime_check(5), '5 should be prime')
        self.assertFalse(prime_check(6), '6 shouldnt be prime')
        self.assertTrue(prime_check(7), '7 should be prime')
        self.assertTrue(prime_check(97), '97 should be prime')

