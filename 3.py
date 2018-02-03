import unittest
import logging
import math


log = logging.getLogger('debug')


# this is way too slow to make work
def generate_primes(maximum):
    """Generate list of primes up to maximum"""
    primes = [2]
    yield 2
    for x in range(3, maximum + 1):
        # the idea here - only things that are divisible by 2, 3 and any other primes are ruled out.  is this right?
        if all([x % prime for prime in primes]):
            primes.append(x)
            yield x


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
    for prime in primes:
        if number % prime == 0:
            return False
    return True


def assignment(number):
    factors = generate_factors(number)
    print('factors: {0}'.format(factors))
    prime_factors = []
    for x in factors:
        if prime_check(x):
            prime_factors.append(x)

    print('prime factors: {0}'.format(prime_factors))
    

def make_primes():
    for i in generate_primes(6008514775143):
        print(i)


if __name__ == '__main__':
    # assignment(13195)
    assignment(600851475143)
    # make_primes()
    # print(generate_factors(6008514775143).sort(key=int))

class Test(unittest.TestCase):
    def test_generate_primes_15(self):
        primes = []
        for x in generate_primes(30):
            primes.append(x)
        self.assertIn(2, primes)
        self.assertIn(3, primes)
        self.assertIn(5, primes)
        self.assertIn(7, primes)
        self.assertIn(11, primes)
        self.assertIn(13, primes)

    def test_generate_primes_30(self):
        primes = []
        for x in generate_primes(30):
            primes.append(x)
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

