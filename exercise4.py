# largest product of two 3-digit numbers = 999 * 999 = 998001
# can find palindromes less than this and factor?

# there is a pattern around how to produce palindromes though
# generate list of palindromes for 3 digit product

import unittest
import math

def is_palindrome(number):
    return str(number) == str(number)[::-1]


def generate_numbers_less(maximum):
    for x in range(maximum, 0, -1):
        yield x


def max_number_for_digits(digits):
    return int(math.pow(10, digits) - 1)


def does_number_have_factors_digits(digits, number):
    """
    Determine if {number} can be the product of two numbers {digits} long
    """
    start = max_number_for_digits(digits)
    stop = max_number_for_digits(digits - 1)
    step = -1
    for x in range(start, stop, step):
        if number % x == 0:
            if len(str(int(number / x))) == len(str(x)):
                return True

    return False


def assignment(maximum, digits):
    for x in generate_numbers_less(maximum):
        if is_palindrome(x):
            if does_number_have_factors_digits(digits, x):
                print(x)
                return x


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(1001))
        self.assertFalse(is_palindrome(91))

    def test_assignment(self):
        self.assertEqual(assignment(99 * 99, 2), 9009)
        assignment(999 * 999, 3)

    def test_max_number_for_digits(self):
        self.assertEqual(max_number_for_digits(2), 99)
        self.assertEqual(max_number_for_digits(3), 999)
    
    def test_does_number_have_factors_digits(self):
        self.assertTrue(does_number_have_factors_digits(2, 100))
