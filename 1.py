import unittest

def exercise(max):
    x = 0
    for y in range(max):
        if y % 3 is 0 or y % 5 is 0:
            x = x + y
    return x


class Test(unittest.TestCase):
    def test_10(self):
       self.assertEqual(exercise(10), 23)

    def test_1000(self):
        print(exercise(1000))

