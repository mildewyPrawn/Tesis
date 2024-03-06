import Point as pt
import Circle as cr
import Delaunay as de
import Triangle as tr
import Edge as ed
import math

p1 = pt.Point(3.897, 0.805) # P
p2 = pt.Point(-2.488, 0.805) # Q
p3 = pt.Point(1.778, 0.805) # F
p4 = pt.Point(-0.587, 0.805) # E
p5 = pt.Point(-3.458, 4.250)
p6 = pt.Point(3.143, 4.847)

d = {}

d[p1] = 'firt pt'
d[p2] = 'second pt'
d[p4] = 'fourth pt'
d[p6] = 'sixth pt'

for key, value in d.items():
    print('{} -> {}'.format(key, value))

print(p5 in d)

print(p1 in d)

p1p = pt.Point(0.805, 3.897)

print(p1p in d)

e = {}

ed1 = ed.Edge(p1, p2)
ed2 = ed.Edge(p3, p4)
ed3 = ed.Edge(p5, p6)

e[ed1] = "first edge"
e[ed2] = "second edge"
e[ed3] = "third edge"

for key, value in e.items():
    print('{} -> {}'.format(key, value))


print(ed1 in e)

print(ed.Edge(p2, p4) in e)

print(ed1 == ed1)

print(ed1 == ed2)

print(ed.Edge(p3, p5) == ed.Edge(p5, p3))

ed4 = ed.Edge(p2, p3)
ed5 = ed.Edge(p4, p1)

print('se tocan? {}'.format(ed4.touch(ed5)))

print(str(ed4.invert()))


