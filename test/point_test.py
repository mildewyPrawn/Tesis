from Circle import *
from Point import *
import math
import random
import unittest

class TestPoint(unittest.TestCase):

    def test_str(self):
        for i in range(0, 100):
            x = i
            y = i*2
            pti = Point(x,y)
            str_pti = '({},{})'.format(x,y)
            self.assertEqual(str(pti), str_pti)

    def test_pos(self):
        for i in range(0, 100):
            x = i
            y = i*2
            pti = Point(x,y)
            self.assertEqual(pti.pos(), [x, y])

    def test_is_equal(self):
        for i in range(0, 100):
            x = i
            y = i*2
            pti = Point(x,y)
            self.assertTrue(pti.is_equal(Point(i, i*2)))
            self.assertFalse(pti.is_equal(Point(y+1,x)), '{} vs {}'.format(pti, Point(y,x)))

    def test_ccw(self):
        for i in range(0, 100):
            x = i
            y = i*2
            a = Point(x,y)
            r = random.randint(0,9) + 1
            b = Point(x+r,y+r)
            c = Point(x+r,y)
            d = Point(x+(2*r), y)
            # check ccw
            self.assertTrue(a.ccw(b,c) < 0, '{}-{}-{} -> {}'.format(a,b,c, a.ccw(b,c)))
            # check cw
            self.assertTrue(c.ccw(b,a) > 0, '{}-{}-{} -> {}'.format(a,b,c, c.ccw(a,b)))
            # check cl
            self.assertTrue(a.ccw(c,d) == 0, '{}-{}-{}'.format(a,b,c))

    def test_distance(self):
        for i in range(0, 100):
            pti = Point(i,i)
            d = math.sqrt((i**2) + (i**2))
            self.assertEqual(pti.distance(Point(0,0)), d, '{} with d = {}'.format(pti, d))

    def test_inside(self):
        for j in range(0, 100):
            r = random.randint(10,100) + j
            c = Circle(xy=Point(r,r), r=10)
            i = random.randint(0,5)
            o = random.randint(10,20)
            inside = Point(r+i, r+i)
            outside = Point(r+o, r+o)
            self.assertTrue(inside.inside(c), '{} inside {}?'.format(inside, c))
            self.assertFalse(outside.inside(c), '{} inside {}?'.format(outside, c))

if __name__ == '__main__':
    unittest.main()
