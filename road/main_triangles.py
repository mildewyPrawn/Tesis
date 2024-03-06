import Point as pt
import Circle as cr
import Delaunay as de
import Triangle as tr
import Edge as ed
import math

p1 = pt.Point(-3, 1)
p2 = pt.Point(-1, 1)
p3 = pt.Point(2, 1)
p4 = pt.Point(4, 1)

t1 = tr.Triangle(p1, p2, p3)
t2 = tr.Triangle(p2, p1, p4)

e1 = ed.Edge(p1, p2)
e2 = ed.Edge(p2, p1)
e3 = ed.Edge(p1, p3)

# print(t1)
# print(t2)

ts = [t1, t2]

a = pt.Point(-3,3)
b = pt.Point(-1,3)
c = pt.Point(-2,1)
d = pt.Point(-3.74, -1.91)
e = pt.Point(-0.4, -1.63)
f = pt.Point(1,1)

ct1 = tr.Triangle(a,b,c)
ct2 = tr.Triangle(a,c,d)
ct3 = tr.Triangle(d,c,e)
ct4 = tr.Triangle(c,f,e)
ct5 = tr.Triangle(f,c,b)

ctss = [ct1, ct2, ct3, ct4, ct5]

for i in range (0, len(ctss)):
    for j in range (i+1, len(ctss)):
        t1 = ctss[i]
        t2 = ctss[j]
        inter_edge = t1.intersect(t2)
        if (inter_edge != None):
            print('{} intersects {} at {}'.format(t1,t2,inter_edge))

'''
1. guardar todas las aristas de los triángulos: DONE
2. para cada pareja de triángulos, si se intersectan DONE
2.1 guardamos una arista de centro a centro DONE
2.2 borramos la arista que los intersecta. DONE
3. Nos quedamos con el CH
4. Usamos lo que ya tenemos para las líneas del CH.
'''

edges_triangles = set()

for tri in ctss:
    edges_triangles.add(tri.ed1)
    edges_triangles.add(tri.ed2)
    edges_triangles.add(tri.ed3)

print('ALL EDGES:')

for e in edges_triangles:
    print(e)

print('Intersections:')

for i in range(0, len(ctss)):
    for j in range(i+1, len(ctss)):
        t1 = ctss[i]
        t2 = ctss[j]
        inter_edge = t1.intersect(t2)
        if (inter_edge != None):
            print('{} intersects'.format(inter_edge))
            edges_triangles.remove(inter_edge)

print('Convex Hull:')

for e in edges_triangles:
    print(e)
