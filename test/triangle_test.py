from Circle import *
from Edge import *
from Pt import *
from Triangle import *
import math
import random
import unittest

class TestTriangle(unittest.TestCase):

    def test_str(self):
        for i in range(0, 99):
            a = Point(i, i)
            b = Point(i+1, i+1)
            c = Point(i+2, i+2)
            e1 = Edge(a,b)
            e2 = Edge(b,c)
            e3 = Edge(c,a)
            t = Triangle(a,b,c)
            str_tri = 'A:{}-B:{}-C:{}'.format(e1,e2,e3)
            self.assertEqual(str(t), str_tri)

    def test_is_equal(self):
        for i in range(0, 99):
            a = Point(i, i)
            b = Point(i+1, i+1)
            c = Point(i+2, i+2)
            t = Triangle(a,b,c)
            t1 = Triangle(a,c,b)
            t2 = Triangle(b,a,c)
            t3 = Triangle(b,c,a)
            t4 = Triangle(c,a,b)
            t5 = Triangle(c,b,a)
            self.assertTrue(t1.is_equal(t2))
            self.assertTrue(t2.is_equal(t3))
            self.assertTrue(t3.is_equal(t4))
            self.assertTrue(t4.is_equal(t5))
            self.assertTrue(t5.is_equal(t1))

if __name__ == '__main__':
    unittest.main()
