import unittest

def even(num):
    return num / 2

def odd(num):
    return 3 * num + 1

def is_even(num):
    return num % 2 == 0

def make_chain(num):
    x = num
    yield x
    while x != 1:
        if is_even(x):
            x = even(x)
            yield x
        else:
            x = odd(x)
            yield x
    yield 1

def assignment():
    winner = 1
    winner_length = 1
    for challenger in range(1,999999):
        challenger_length = len(list(make_chain(challenger)))
        if challenger_length > winner_length:
            print('{0}: {1}'.format(winner, winner_length))
            winner = challenger
            winner_length = challenger_length
    
    print(winner)
    print(winner_length)

if __name__ == '__main__':
    assignment()

class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(list(make_chain(13)), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(len(list(make_chain(13))), 10)