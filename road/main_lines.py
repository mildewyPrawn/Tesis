import Point as pt
import Circle as cr
import Delaunay as de
import Triangle as tr
import Vor as vor
import Edge as ed
import math

def draw_semi_lines(coord1, coord2, origin):
    return [ed.Edge(coord1, origin), ed.Edge(coord2, origin)]

def calculate_parallels(pt1, pt2, circ, epsilon=0.054303604523999995):
    midPT = pt1.middle_point(pt2)
    # print('mid point is: {}'.format(midPT))
    ed12 = ed.Edge(pt1, pt2)
    m, b = ed12.get_equation()
    # print('slope [{},{}] is: {}'.format(pt1, pt2, ed12.get_slope()))
    distance_to_origin = midPT.distance(circ.origin)
    # lineas paralelas a Y
    if (math.isnan(ed12.get_slope())):
        cx = circ.origin.x
        # print('y = {}'.format(midPT.y))
        # print('x = {}'.format(pt1.x))
        # print('Epsilon = {}\n1. x = {}\n2. x = {}'.format(epsilon, cx - circ.radius, cx + circ.radius)) # lineas paralelas
        return draw_semi_lines(pt.Point(cx - circ.radius, midPT.y), pt.Point(cx + circ.radius, midPT.y), circ.origin)
        # return ((cx - circ.radius, midPT.y), (cx + circ.radius, midPT.y))
    # lineas paralelas a X
    if (ed12.get_slope() == 0):
        cy = circ.origin.y
        # print('y = {}'.format(pt1.y))
        # print('x = {}'.format(midPT.x))
        # print('Epsilon = {}\n1. y = {}\n2. y = {}'.format(epsilon, cy - circ.radius, cy + circ.radius)) # lineas paralelas
        return draw_semi_lines(pt.Point(midPT.x, cy - circ.radius), pt.Point(midPT.x, cy + circ.radius), circ.origin)
        # return ((midPT.x, cy - circ.radius), (midPT.x, cy + circ.radius))
    mP = -1 * (1 / m)
    bP = (-1 * mP * midPT.x) + midPT.y
    # print('y = {}x + {}'.format(m, b))
    # print('m-- = {}x + {}'.format(mP, bP))
    pa = m
    pb = -1
    c1 = b
    d = circ.radius
    # print('distance to origin = {}'.format(distance_to_origin))
    # ajustar el centro, solo cuando no es igual al origen
    if distance_to_origin != 0:
        # a veces recorremos pa'rriba, otras pa'bajo
        c1 = c1 + (distance_to_origin if m < 0 else (-1 * distance_to_origin))
    else:
        c1 = c1 + (epsilon if m > 0 else (-1 * epsilon))
    # print('0 = {}x + {}y + {}'.format(pa, pb, c1))
    ab = math.sqrt((pa**2) + (pb**2))
    minus = (-1 * ((d * ab) - c1)) + (epsilon if m < 0 else (-1 * epsilon))
    mayus = (-1 * ((d * (-1 * ab)) - c1)) + (epsilon if m < 0 else (-1 * epsilon))
    # print('Epsilon = {}\n1. y = {}x + {}\n2. y = {}x + {}'.format(epsilon, m, minus-epsilon, m, mayus-epsilon)) # lineas paralelas
    intXminus = ((-1 * minus) - (-1 * bP)) / ((mP * -1) - (m * -1))
    intYminus = ((m * bP) - (mP * minus)) / ((mP * -1) - (m * -1))
    intXmayus = ((-1 * mayus) - (-1 * bP)) / ((mP * -1) - (m * -1))
    intYmayus = ((m * bP) - (mP * mayus)) / ((mP * -1) - (m * -1))
    return draw_semi_lines(pt.Point(intXminus, intYminus), pt.Point(intXmayus, intYmayus), circ.origin)
    # return ((intXminus, intYminus), (intXmayus, intYmayus))

def lines_from_circle(tr, circ):
    a = tr.a.p1
    b = tr.b.p1
    c = tr.c.p1
    lines = calculate_parallels(a, b, circ) + calculate_parallels(b, c, circ) + (calculate_parallels(c, a, circ))
    return lines


circ = cr.Circle(xy=pt.Point(4.318, 2.045), r=3.318)
pt1 = pt.Point(7,4)
pt2 = pt.Point(1,2)
pt3 = pt.Point(7,0.0920744370266)

t1 = tr.Triangle(ed.Edge(pt1, pt2), ed.Edge(pt2, pt3), ed.Edge(pt3, pt1))

# lines = calculate_parallels(pt1, pt2, circ)
lines = lines_from_circle(t1, circ)
for l in lines:
    print('line: {}'.format(l))

# print('The coordinates are: ({}, {})'.format(xm, ym))
# print('The coordinates are: ({}, {})'.format(xM, yM))

print()

# ((xm2, ym2), (xM2, yM2)) = calculate_parallels(pt1, pt3, circ)

# print('The coordinates are: ({}, {})'.format(xm2, ym2))
# print('The coordinates are: ({}, {})'.format(xM2, yM2))

print()
# ((xm3, ym3), (xM3, yM3)) = calculate_parallels(pt2, pt3, circ)

# print('The coordinates are: ({}, {})'.format(xm3, ym3))
# print('The coordinates are: ({}, {})'.format(xM3, yM3))


print()
print()
print()


pt4 = pt.Point(-2, 3)
pt5 = pt.Point(2, 3)
pt6 = pt.Point(2, -1)

circ2 = cr.Circle(a=pt4, b=pt5, c=pt6)
origen, radio = circ2.circumcircle()
# print('circulo con origen en: {} y radio: {}\n\n'.format(origen, radio))

# ((xm4, ym4), (xM4, yM4)) = calculate_parallels(pt4, pt5, circ2)

# print('The coordinates are: ({}, {})'.format(xm4, ym4))
# print('The coordinates are: ({}, {})'.format(xM4, yM4))

print()
# ((xm5, ym5), (xM5, yM5)) = calculate_parallels(pt4, pt6, circ2)

# print('The coordinates are: ({}, {})'.format(xm5, ym5))
# print('The coordinates are: ({}, {})'.format(xM5, yM5))

print()
# ((xm6, ym6), (xM6, yM6)) = calculate_parallels(pt5, pt6, circ2)

# print('The coordinates are: ({}, {})'.format(xm6, ym6))
# print('The coordinates are: ({}, {})'.format(xM6, yM6))



