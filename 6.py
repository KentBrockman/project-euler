# https://www.pythoncentral.io/time-a-python-function/

import unittest
import math

def square_of_sum(number):
    return sum([x for x in range(1,number + 1,1)]) ** 2

def sum_of_squres(number):
    return sum([x ** 2 for x in range(1,number + 1,1)])


class Tests(unittest.TestCase):
    def test_square_of_sums(self):
        self.assertEqual(square_of_sum(10), 3025)

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squres(10), 385)

    def test_assignment(self):
        self.assertEqual(square_of_sum(10) - sum_of_squres(10), 2640)
        print(square_of_sum(100) - sum_of_squres(100))
