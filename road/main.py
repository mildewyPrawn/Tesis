import Point as pt
import Circle as cr

a = pt.Point(11, 11)
b = pt.Point(13, 9)
c = pt.Point(13, 11)
d = pt.Point(12, 7)
e = pt.Point(10, 9)
f = pt.Point(15, 10)

l = [a,b,c,d,e,f]

vor = Voronoi(l)
vor.process()
edges = vor.get_output()
for edge in edges:
    print(edge)

print('ends')

c1 = cr.Circle(a=b,b=a,c=c)
c1.circumcircle()
# print('radius: {} at {}'.format(r1, o1))
print(c1)

r, c2 = vor.circle(b, a, c)

print('radius: {} at {}'.format(r, c2))

'''
two lines are parallel if their slopes are equal.
'''
