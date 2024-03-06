import Circle as cr
import Delaunay as de
import Edge as ed
import Point as pt
import Triangle as tr
import Vor as vor
import math

class Teselation:

    '''Constructor de la clase, recibimos todos los triangulos posibles'''
    def __init__(self, triangles):
        self.triangles = triangles

    def process_intersection(self):
        lines = []
        edges_triangles = set()

        for tri in self.triangles:
            edges_triangles.add(tri.ed1)
            edges_triangles.add(tri.ed2)
            edges_triangles.add(tri.ed3)

        for i in range(0, len(self.triangles)):
            for j in range(i+1, len(self.triangles)):
                t1 = self.triangles[i]
                t2 = self.triangles[j]
                c1 = cr.Circle(a=t1.a, b=t1.b, c=t1.c)
                c2 = cr.Circle(a=t2.a, b=t2.b, c=t2.c)
                (o1, _) = c1.circumcircle()
                (o2, _) = c2.circumcircle()
                inter_edge = t1.intersect(t2)
                if (inter_edge != None and inter_edge in edges_triangles):
                    print('{} intersects'.format(inter_edge))
                    edges_triangles.remove(inter_edge)
                    lines.append(ed.Edge(o1, o2))

        '''hasta aqui ya tenemos todas las  que no estan en el cierre convexo,
        ahora lo que queremos es las del cierre.

        Necesito: el triangulo, la arista y los puntos. y la funcion clean_segments
        '''

        for tri in self.triangles:
            e1 = tri.ed1
            e2 = tri.ed2
            e3 = tri.ed3
            a = tri.a
            b = tri.b
            c = tri.c
            circle = cr.Circle(a=tri.a, b=tri.b, c=tri.c)
            if (e1 in edges_triangles):
                lines = lines + self.clean_segments(circle, e1, a,b,c)
                edges_triangles.remove(e1)
            if (e2 in edges_triangles):
                lines = lines + self.clean_segments(circle, e2, b,c,a)
                edges_triangles.remove(e2)
            if (e3 in edges_triangles):
                lines = lines + self.clean_segments(circle, e3, c,a,b)
                edges_triangles.remove(e3)

        return lines

    '''metodo que dado un circulo creado por los puntos a,b,c y una arista
    (ab, bc,  ca) nos regresa unicamente  la (mitad de la)  arista que
    nos interesa. La forma de hacer esto es que si a-b-c estan en ccw,
    entonces calculamos los dos posibles  puntos pt1 y pt2. Si a-b-pt1
    esta en ccw, entonces la arista importante es pt2-o (donde o es el
    origen del circulo). En otro caso agregamos la arista pt1-o'''
    def clean_segments(self, circle, edge, a, b, c):
        v_pts = self.inter_cl(circle, edge)
        pt1 = v_pts[0]
        pt2 = v_pts[1]
        pts = a.ccw(b,c)
        pts_pt1 = a.ccw(b, pt1)
        pts_pt2 = a.ccw(b, pt2)
        if (pts < 0 and pts_pt1 < 0):
            return [ed.Edge(circle.origin, pt2)]
        elif (pts < 0 and pts_pt2 < 0):
            return [ed.Edge(circle.origin, pt1)]
        elif (pts > 0 and pts_pt1 < 0):
            return [ed.Edge(circle.origin, pt1)]
        else:
            return [ed.Edge(circle.origin, pt2)]

    '''interseccion de una linea con un circulo de radio r con centro en el origen
    https://cp-algorithms.com/geometry/circle-line-intersection.html
    TODO: el problema es que el circulo esta en el origen'''
    def intersection(self, line, r):
        (a,b,c) = line.get_mediatrix()
        # (sx, sy, x, y, r) = get_equation_circ()
        x0 = -a*c/(a*a+b*b)
        y0 = -b*c/(a*a+b*b)
        d = r*r - c*c/(a*a+b*b)
        mult = math.sqrt(d / (a*a+b*b));
        ax = x0 + b * mult;
        bx = x0 - b * mult;
        ay = y0 - a * mult;
        by = y0 + a * mult;
        print('({},{}) and ({}, {})'.format(ax, ay, bx, by))


    def cuad(self, a,b,c):
        if (b != 0):
            return (-1 * (a/b), -1 * (c/b))
        else:
            return (-1 * a,-1 * c)

    def chicharronera(self, a,b,c):
        sqr = math.sqrt(b**2 - (4 * a * c))
        res = -1 * b
        return ((res + sqr)/(2*a), (res - sqr)/(2*a))

    '''TODO: para las  dos aristas creadas, calcular el midpoin  de line y
    se queda solo la arista que lo contiene.

    NEW TODO: Si la interseccion de una con otra es el punto medio, la agrego
    '''
    def inter_cl(self, circle, line):
        mid = line.p1.middle_point(line.p2)
        (a,b,c) = line.get_mediatrix() # ax + by + c = 0
        x, y, xs, ys, r = circle.get_equation_circ() # x2 + y2 + x + y + r = 0
        a,c = self.cuad(a,b,c) #ax/b + c/b
        # x2 + (ax/b + c/b)2 + x + (ax/b + c/b) + r = 0
        x = x + (a**2)
        r = r + (c**2) + (c * ys)
        xs = xs + (2 * a * c) + (a * ys)#x
        x1, x2 = self.chicharronera(x,xs,r)
        y1 = a*x1 + c
        y2 = a*x2 + c
        # return (pt.Point(x1,y1), pt.Point(x2,y2))
        p1 = pt.Point(x1, y1)
        p2 = pt.Point(x2, y2)
        return (p1, p2)
        # return [ed.Edge(p1, circle.origin), ed.Edge(p2, circle.origin)]






    '''Para cada triangulo, sacar su cicunferencia y mandar a calcular las
    parelalas'''

    '''TODO: las aristas no quedan donde deberian'''
    def process(self):
        lines = []
        for tr in self.triangles:
            a = tr.a
            b = tr.b
            c = tr.c
            circle = cr.Circle(a=a, b=b, c=c)
            o, r = circle.circumcircle()
            lines = lines + self.lines_from_circle(tr, circle)
            # print('triangle = {}\nCircle = {}\n'.format(tr, circle))
        print('DESDE LA TESELATION: {}'.format(len(lines)))
        return lines

    def draw_semi_lines(self, coord1, coord2, origin):
        return [ed.Edge(coord1, origin), ed.Edge(coord2, origin)]

    def calculate_parallels(self, pt1, pt2, circ, epsilon=0.054303604523999995):
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
            return self.draw_semi_lines(pt.Point(cx - circ.radius, midPT.y), pt.Point(cx + circ.radius, midPT.y), circ.origin)
        # return ((cx - circ.radius, midPT.y), (cx + circ.radius, midPT.y))
        # lineas paralelas a X
        if (ed12.get_slope() == 0):
            cy = circ.origin.y
            # print('y = {}'.format(pt1.y))
            # print('x = {}'.format(midPT.x))
            # print('Epsilon = {}\n1. y = {}\n2. y = {}'.format(epsilon, cy - circ.radius, cy + circ.radius)) # lineas paralelas
            return self.draw_semi_lines(pt.Point(midPT.x, cy - circ.radius), pt.Point(midPT.x, cy + circ.radius), circ.origin)
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
        return self.draw_semi_lines(pt.Point(intXminus, intYminus), pt.Point(intXmayus, intYmayus), circ.origin)
    # return ((intXminus, intYminus), (intXmayus, intYmayus))

    def calculate_parallels_2(self, pt1, pt2, circ):
        pass

    def lines_from_circle(self, tr, circ):
        a = tr.a
        b = tr.b
        c = tr.c
        lines = self.calculate_parallels(a, b, circ) + self.calculate_parallels(b, c, circ) + self.calculate_parallels(c, a, circ)
        print('----------------------------------------')
        print('The circle with {},{},{} has origin in {} and radius {}'.format(a,b,c,circ.origin,circ.radius))
        print('The 6 lines are:')
        for l in lines:
            print(l)
        print('----------------------------------------')
        return lines
