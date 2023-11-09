from Edge import *
from Point import *
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

    def test_slope(self):
        p1 = Point(-5,15)
        p2 = Point(-10,18)
        s1 = -3/5
        e1 = Edge(p1, p2)
        e2 = Edge(p2, p1)
        p3 = Point(6, -8)
        p4 = Point(14, -8)
        s2 = -3/5
        e3 = Edge(p3, p4)
        e4 = Edge(p4, p3)
        s2 = 0.0
        self.assertTrue(e1.get_slope() == s1, '{} vs {}'.format(e1.get_slope(), s1))
        self.assertTrue(e2.get_slope() == s1, '{} vs {}'.format(e1.get_slope(), s1))
        self.assertTrue(e3.get_slope() == s2, '{} vs {}'.format(e3.get_slope(), s2))
        self.assertTrue(e4.get_slope() == s2, '{} vs {}'.format(e4.get_slope(), s2))

if __name__ == '__main__':
    unittest.main()
