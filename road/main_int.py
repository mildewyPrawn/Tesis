import Point as pt
import Circle as cr
import Delaunay as de
import Triangle as tr
import Vor as vor
import Edge as ed
import math

'''ecuacion chida para  calcular una recta de  la forma ax + by  + c = 0'''
def get_equation(pt1, pt2):
    a = pt2.y - pt1.y
    b = pt1.x - pt2.x
    c = pt1.y*pt2.x - pt1.x*pt2.y
    return (a,b,c)

'''ecuacion  chida para  calcular la  madiatriz de  un segmento  de la
forma ax + by + c = 0'''
def get_mediatrix(pt1, pt2):
    a1 = pt1.x
    b1 = pt1.y
    a2 = pt2.x
    b2 = pt2.y
    x = -1 * (a1*2) + (a2*2)
    y = -1 * (b1*2) + (b2*2)
    c = (a1**2 + b1**2) - (a2**2 + b2**2)
    return (x, y, c)

'''ecuacion chida para calcular un círculo de la forma (x – h)² + (y – k)² = r²
regresa: (x², y², -2xh, -2yk, -r2+h²+k²)'''
def get_equation_circ(circ):
    o, r = circ.circumcircle()
    h = o.x
    k = o.y
    x = (-1 * h * 2)
    y = (-1 * k * 2)
    r = (-1 * r**2) + (h**2) + (k**2)
    return (1,1,x,y,r)

'''interseccion de una linea con un círculo de radio r con centro en el origen
https://cp-algorithms.com/geometry/circle-line-intersection.html
TODO: el problema es que el circulo está en el origen'''
def intersection(line, r):
    (a,b,c) = get_mediatrix(line.p1, line.p2)
    # (sx, sy, x, y, r) = get_equation_circ(circ)
    x0 = -a*c/(a*a+b*b)
    y0 = -b*c/(a*a+b*b)
    d = r*r - c*c/(a*a+b*b)
    mult = math.sqrt(d / (a*a+b*b));
    ax = x0 + b * mult;
    bx = x0 - b * mult;
    ay = y0 - a * mult;
    by = y0 + a * mult;
    print('({},{}) and ({}, {})'.format(ax, ay, bx, by))


def cuad(a,b,c):
    if (b != 0):
        return (-1 * (a/b), -1 * (c/b))
    else:
        return (-1 * a,-1 * c)

def chicharronera(a,b,c):
    sqr = math.sqrt(b**2 - (4 * a * c))
    res = -1 * b
    return ((res + sqr)/(2*a), (res - sqr)/(2*a))

def inter_cl(circle, line):
    (a,b,c) = get_mediatrix(line.p1, line.p2) # ax + by + c = 0
    x, y, xs, ys, r = get_equation_circ(circle) # x² + y² + x + y + r = 0
    a,c = cuad(a,b,c) #ax/b + c/b
    # x² + (ax/b + c/b)² + x + (ax/b + c/b) + r = 0
    x = x + (a**2)
    r = r + (c**2) + (c * ys)
    xs = xs + (2 * a * c) + (a * ys)#x
    x1, x2 = chicharronera(x,xs,r)
    y1 = a*x1 + c
    y2 = a*x2 + c
    # return (pt.Point(x1,y1), pt.Point(x2,y2))
    return [ed.Edge(pt.Point(x1, y1), circle.origin), ed.Edge(pt.Point(x2, y2), circle.origin)]

def process_intersection(circle, triangle):
    e1 = triangle.ed1
    e2 = triangle.ed2
    e3 = triangle.ed3
    lines = inter_cl(circle, e1) + inter_cl(circle, e2) + inter_cl(circle, e3)
    print('----------')
    for l in lines:
        print(l)
    print('----------')
    return lines

p1 = pt.Point(250, 250)
p2 = pt.Point(300, 350)
p3 = pt.Point(250, 450)

t1 = tr.Triangle(p1, p2, p3)
c1 = cr.Circle(a=p1, b=p2, c=p3)
o,r = c1.circumcircle()

print(get_equation(p1,p2))
print(get_mediatrix(p1,p2))

print(get_equation(p2,p3))
print(get_mediatrix(p2,p3))

print(get_equation(p3,p1))
print(get_mediatrix(p3,p1))

print('The center is: {} and the radius is: {}'.format(o,r))
print(get_equation_circ(c1))

# inter_cl(c1, ed.Edge(p1, p2))
# inter_cl(c1, ed.Edge(p2, p3))
# inter_cl(c1, ed.Edge(p3, p1))

print(process_intersection(c1, t1))
