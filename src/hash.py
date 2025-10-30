import Triangle as tr
import Point as pt

import numpy as np
from scipy.spatial import Delaunay

p1 = pt.Point(-1.5, -2)
p2 = pt.Point(5.5, 10.29)
p3 = pt.Point(12.59, -2)

t1 = tr.Triangle(p1, p2, p3)
t2 = tr.Triangle(p2, p1, p3)
t3 = tr.Triangle(p2, p3, p1)
t4 = tr.Triangle(p3, p2, p1)

print(hash(t1))
print(hash(t2))
print(hash(t3))
print(hash(t4))

root_triangle = tr.Triangle(p1, p2, p3)
outer_triangle = set(root_triangle)

print('------------------------------')
points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
tri = Delaunay(points)
print(tri)
print(type(tri))
