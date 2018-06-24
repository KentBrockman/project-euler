import unittest
import itertools

# lets treat the grid like an acyclic graph
# have a class for each node in the grid

# TODO: refactor: https://stackoverflow.com/questions/19130986/python-equivalent-of-golangs-select-on-channels
# more reading for interest: http://interactivepython.org/runestone/static/pythonds/Trees/VocabularyandDefinitions.html
# https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8

class Node:
    def __init__(self, size, x=0, y=0):
        self.size = size
        self.x = x
        self.y = y

        self.children = []

        if x + 1 < size + 1:
            self.children.append(Node(size, x + 1, y))
        
        if y + 1 < size + 1:
            self.children.append(Node(size, x, y + 1))
    
    def isBottom(self):
        return len(self.children) == 0

    def howManyChildren(self):
        if self.isBottom():
            return 1

        return sum([x.howManyChildren() for x in self.children])

class Tests(unittest.TestCase):
    def test_2(self):
        self.assertEqual(Node(2).howManyChildren(), 6)
        print(Node(2).howManyChildren())
        print(Node(3).howManyChildren())
        print(Node(4).howManyChildren())
        print(Node(5).howManyChildren())
        
        # BUG: too slow at 20....
        # print(Node(20).howManyChildren())
