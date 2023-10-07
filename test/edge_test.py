from Edge import *
from Pt import *
import math
import random
import unittest

class TestEdge(unittest.TestCase):

    def test_str(self):
        for i in range(0, 100):
            p1 = Point(i, i)
            p2 = Point(i*2, i*2)
            e  = Edge(p1, p2)
            s  = '({},{})-({},{})'.format(i,i, i*2,i*2)
            self.assertTrue(str(e), s)

    def test_is_equal(self):
        for i in range(0, 100):
            p1 = Point(i, i)
            p2 = Point(i*2, i*2)
            p3 = Point(i+i+10, i+i)
            e1 = Edge(p1, p2)
            e2 = Edge(p2, p1)
            e3 = Edge(p1, p3)
            self.assertTrue(e1.is_equal(e2), '{} vs {}'.format(e1, e2))
            self.assertFalse(e1.is_equal(e3), '{} vs {}'.format(e1, e3))

    def test_length(self):
        for i in range(0, 100):
            r = random.randint(0,10)
            p1 = Point(0,0)
            p2 = Point(0,i+r)
            e  = Edge(p1, p2)
            self.assertEqual(e.length(), i+r)

    def test_edge_intersection(self):
        for i in range(1, 100):
            r = random.randint(2,200)
            p1 = Point(0,0)
            p2 = Point(0,i+(r*2))
            p3 = Point((-1)*i, i+r)
            p4 = Point(i, i+r)
            p5 = Point(r, 0)
            p6 = Point(r, i+(r*2))
            e1 = Edge(p1,p2)
            e2 = Edge(p3,p4)
            e3 = Edge(p5, p6)
            self.assertTrue(e1.edge_intersection(e2), '{} intersect {}'.format(e1, e2))
            self.assertFalse(e1.edge_intersection(e3), '{} intersect {}'.format(e1, e2))

if __name__ == '__main__':
    unittest.main()
