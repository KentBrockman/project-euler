# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import unittest
import itertools
import math

def prime_generator(stopAt=-1):
    numberOn = 2
    primes = []
    while stopAt is -1 or numberOn < stopAt:
        # make a generator for the valid primes to check
        valid_primes = itertools.filterfalse(lambda x: x > math.sqrt(numberOn), primes)

        # now check if the number youre on is divisible by any of these
        isPrime = True
        for prime in valid_primes:
            # quit the instant you find a prime that divides the number in question
            if numberOn % prime == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(numberOn)
            yield numberOn

        numberOn = numberOn + 1


def assignment(which_prime):
    primes = prime_generator()

    for x in range(which_prime - 1):
        next(primes)

    return next(primes)

class Tests(unittest.TestCase):
    def test_prime_generator(self):
        gen = prime_generator(10)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 5)

    def test_assignment(self):
        self.assertEqual(assignment(6), 13)
        print(assignment(10001))
