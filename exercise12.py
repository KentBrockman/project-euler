import unittest
import math

def triangle_numbers():
    """
    generator that returns triangle numbers
    """
    start = 0
    ret = 0
    while True:
        start = start + 1
        ret = ret + start
        yield ret

def generate_factors(num):
    maxloop = int(math.ceil(math.sqrt(num)))
    factors = []
    for x in range(1, maxloop):
        if num % x == 0:
            factors.append(x)
            factors.append(num / x)
    return factors

def assignment(num_of_divisors):
    for triangle_number in triangle_numbers():
        factors = generate_factors(triangle_number)
        if len(factors) > num_of_divisors:
            return triangle_number

class Tests(unittest.TestCase):
    def test_triangle_number(self):
        gen = triangle_numbers()
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 6)
        self.assertEqual(next(gen), 10)
        self.assertEqual(next(gen), 15)
        self.assertEqual(next(gen), 21)
 
    def test_generate_factor(self):
         self.assertEqual(len(generate_factors(28)), 6)

    def test_assignment(self):
        self.assertEqual(assignment(5), 28)
        print(assignment(500))
