from Circle import *
from Point import *
import math
import random
import unittest

class TestCircle(unittest.TestCase):

    def test_str(self):
        for i in range(0, 100):
            r = random.randint(0,9) + 1
            p = Point(i, i+r)
            c = Circle(p, 10)
            str_circ = str(p) + ' at 10 coll NoneNoneNone'
            self.assertEqual(str(c), str_circ)

    def test_circumcircle(self):
        c = Circle(a=Point(1,1), b=Point(2,4), c=Point(5,3))
        p, r = c.circumcircle()
        pf = Point(3.0,2.0)
        self.assertEqual(pf.x, p.x, '{} vs {}'.format(p.x, pf.x))
        self.assertEqual(pf.y, p.y, '{} vs {}'.format(p.y, pf.y))
        self.assertEqual(r, math.sqrt(5))
        c = Circle(a=Point(250,450), b=Point(300,350), c=Point(400,450))
        p, r = c.circumcircle()
        pf = Point(325, 425)
        self.assertEqual(pf.x, p.x, '{} vs {}'.format(p.x, pf.x))
        self.assertEqual(pf.y, p.y, '{} vs {}'.format(p.y, pf.y))
        self.assertEqual(round(r, 2), round(158.1138/2, 2))

    def test_determinant_2x2(self):
        c = Circle(Point(0,0), 10)
        d = c.determinant_2x2(1,2,3,4)
        self.assertEqual(d, -2)
        d = c.determinant_2x2(-1, -2, 6, 3)
        self.assertEqual(d, 9)

    def test_determinant_3x3(self):
        c = Circle(Point(0,0), 10)
        d = c.determinant_3x3(2, -3, 1, 2, 0, -1, 1, 4, 5)
        self.assertEqual(d, 49)
        d = c.determinant_3x3(-5, -5, -5, 3, -1, -2, 4, 2, 1)
        self.assertEqual(d, -10)

if __name__ == '__main__':
    unittest.main()
