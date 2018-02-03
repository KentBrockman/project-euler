# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import unittest

def assignment(rangeToDivideBy, startWith=0):
    print(startWith)
    tryMe = startWith if startWith > 0 else max(rangeToDivideBy)
    factors = rangeToDivideBy
    matches = 0
    step = min(rangeToDivideBy)
    
    # find first number divisible by min
    while tryMe % step:
        tryMe = tryMe + 1

    # then start searching taking steps of the smallest factor to guarantee disibility of the smallest factor
    # this is all to cut down on the number of computations to perform
    while matches < len(factors):
        print(tryMe)
        # step with minimum size in the range
        tryMe = tryMe + step
        matches = 0
        for factor in factors:
            if tryMe % factor == 0:
                matches = matches + 1

    return tryMe


if __name__ == '__main__':
   secondRange = [
       # 1, this is always true
       # 2, covered by 10
       # 3, covered by 9
       # 4, covered by 16
       # 5, covered by 10, 15
       # 6, covered by 12
       # 7, covered by 14
       # 8, covered by 16
       # 9, covered by 18
       # 10, covered by 20
       11,
       12,
       13,
       14,
       15,
       16,
       17,
       18,
       19,
       20
   ]
   print(assignment(secondRange, 109360816)) # tried everything up until then, took 00:06:34
   # got the answer 232792560 in an addition 00:01:17.25


class Test(unittest.TestCase):
    def test_understand_list_copy(self):
        lis1 = [1,2,3,4,5]
        lis2 = lis1[:]
        lis2.remove(3)
        self.assertIn(3, lis1)
        self.assertNotIn(3, lis2)

        for x in lis1:
            lis1.remove(x)

        self.assertFalse(0, len(lis1))

    def test_assignment(self):
        # compress the list to do less math
        # if any number lower on the list is a factor of any number higher on the list, you can remove it
        # this is because if any number is divisible by a higher number in the list, the factor automatically gets a pass.  if the lower number passes but the higher one doesnt, the number will still not pass, so only bother testing the highs
        firstRange = [
            # 1, this is always true
            # 2, covered by 10
            # 3, covered by 9
            4, 
            # 5, covered by 10
            6,
            7,
            8,
            9,
            10,
        ]
        self.assertEqual(assignment(firstRange), 2520)
        # secondRange = [
            # 1, this is always true
            # 2, covered by 10
            # 3, covered by 9
            # 4, covered by 16
            # 5, covered by 10, 15
            # 6, covered by 12
            # 7, covered by 14
            # 8, covered by 16
            # 9, covered by 18
            # 10, covered by 20
            # 11,
            # 12,
            # 13,
            # 14,
            # 15,
            # 16,
            # 17,
            # 18,
            # 19,
            # 20
        # ]
        # print(assignment(secondRange))

