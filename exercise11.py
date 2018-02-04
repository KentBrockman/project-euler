import unittest
import itertools
import functools

# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

grid = [
[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
]

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def get(x,y):
    return grid[y][x]

def read_down(digits, x, y):
    seq = []
    for i in range(y, y+digits, 1):
        if i < 20: # dont go outside bounds of the grid
           seq.append(get(x,i))
    return seq

def read_right(digits, x, y):
    seq = []
    for i in range(x, x+digits, 1):
        if i < 20: # dont go outside bounds of the grid
           seq.append(get(i,y))
    return seq

def read_se_diagonal(digits, x, y):
    seq = []
    for i,j in zip(range(x, x+digits, 1), range(y, y+digits, 1)):
        if i < 20 and j < 20: # dont go outside bounds of the grid
           seq.append(get(i,j))
    return seq

def read_ne_diagonal(digits, x, y):
    seq = []
    for i,j in zip(range(x, x+digits, 1), range(y, y-digits, -1)):
        if i < 20 and j > -1: # dont go outside bounds of the grid
           seq.append(get(i,j))
    return seq

def product(seq):
    return functools.reduce(lambda x,y: x*y, seq)

def assignment():
    digits = 4
    # only need these functions.  any read_up sequences will also be make by read_down.  any read_right sequences will be produced by read_left, same goes for the diagonal reads
    functions = [ read_right, read_down, read_se_diagonal, read_ne_diagonal ]
    winner = 0
    for x,y in itertools.product(range(20), range(20)):
        for func in functions:
           seq = func(digits, x, y)
           challenger = product(seq)
           # print(x,y,seq, func.__name__, challenger)
           if challenger > winner:
               print(x,y,seq, func.__name__, challenger)
               winner = challenger
    return winner

if __name__ == '__main__':
    print(assignment())

class Tests(unittest.TestCase):
    def test_assignment(self):
        # TODO: verify the read_* methods, it looks like we are getting sequences that might not be real?
        # TODO: reevaluate how youre indexing the grid.  i think your x and y are inverted on the array index
        assignment()
        
    def test_read_down(self):
        seq = read_down(4,3,3)
        self.assertEqual(seq, [23, 71, 60, 28])

        seq = read_down(4,0,19)
        self.assertEqual(1, len(seq))

    def test_read_right(self):
        seq = read_right(4,3,3)
        self.assertEqual(seq, [23, 4, 60, 11])
        
        seq = read_right(4,19,0)
        self.assertEqual(1, len(seq))

    def test_read_se_diagonal(self):
        seq = read_se_diagonal(4,0,0)
        self.assertEqual(seq, [8, 49, 31, 23])

        seq = read_se_diagonal(4,8,6)
        self.assertEqual(seq, [26, 63, 78, 14])

        seq = read_se_diagonal(4,19,19)
        self.assertEqual(1, len(seq))

    def test_nested_ranges(self):
        lis = [(x,y) for x, y in zip(range(3), range(3))]
        self.assertEqual(lis[0], (0,0))
        self.assertEqual(lis[1], (1,1))
        self.assertEqual(lis[2], (2,2))

    def test_product(self):
        self.assertEqual(product([2,2,2]), 8)
        self.assertEqual(product([26,63,78,14]), 1788696)

    def test_get_number(self):
        self.assertEqual(get(10,10), 3)
        self.assertEqual(get(8,6), 26)
        
    def test_example(self):
        self.assertEqual(product(read_se_diagonal(4,8,6)), 1788696)
