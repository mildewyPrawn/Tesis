import Point as pt
import Circle as cr
import Delaunay as de
import Triangle as tr
import Edge as ed
import math

edges = []

p1 = pt.Point(-3, 1)
p2 = pt.Point(-1, 1)
p3 = pt.Point(2, 1)
p4 = pt.Point(4, 1)

ed1 = ed.Edge(p1, p3)
ed2 = ed.Edge(p2, p4)

edges.append(ed1)
edges.append(ed2)

# for e in edges:
    # print(e)

complete = []

for i in range(len(edges)):
    flag = False
    for j in range(i+1, len(edges)):
        ed1 = edges[i]
        ed2 = edges[j]
        if (ed1.p1.ccw(ed2.p1, ed2.p2) == 0):
            complete.append(ed.Edge(ed1.p2, ed2.p1))
            # flag = not flag
            i = i + 1
            j = j + 1
            break
    if (flag):
        complete.append(edges[i])
        # print('compare {} vs {}'.format(edges[i], edges[j]))

for c in complete:
    print(c)


