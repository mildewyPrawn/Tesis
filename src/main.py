import Triangle as tr
import Point as pt
import DelaunayBW as delbw

p1 = pt.Point(-3,1, 'A')
p2 = pt.Point(-1,2, 'B')
p3 = pt.Point(1,0,  'C')

t1 = tr.Triangle(p1, p2, p3)

p4 = pt.Point(-3,-1, 'D')

p5 = pt.Point(-1,-1, 'E')

print(p4 in t1)
print(p1 in t1)
print(p5 in t1)

t2 = tr.Triangle(p2, p1, p3)

print(hash(t1))
print(hash(t2))

print('----------------------------------------')
pts = [p1, p2, p3, p4, p5]
delaunay = delbw.DelaunayBW(pts)
triangs = delaunay.get_triangulation()

print(triangs)
print('---------------------------------------->>>>')
# p = pt.Point(-2, 1, 'new')
# triangs = delaunay.update(p)

print(triangs)
# p = p2
# for t in triangs:
#     if p in t:
#         print('Hey')
