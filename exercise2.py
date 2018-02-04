import unittest

def exercise(maximum):
    fibonacci = [1, 2]
    x = 0
    while fibonacci[-1] < maximum:
        # check the last element - if even, add to the sum total
        if fibonacci[-1] % 2 is 0:
            x = x + fibonacci[-1]

        # generate a new number for the fibonnaci sequence
        newnum = sum([fibonacci[-2], fibonacci[-1]])

        # add it to the fibonacci sequence
        fibonacci.append(newnum)

        # while condition = keep going until you hit the max

    return x


class Test(unittest.TestCase):
    def test_10(self):
        self.assertEqual(exercise(10), 10)

    def test_35(self):
        self.assertEqual(exercise(35), 2 + 8 + 34)

    def test_answer(self):
        print('Answer is {0}'.format(exercise(4 * 10**6)))

