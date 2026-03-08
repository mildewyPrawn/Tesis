import Circle as cr
import Delaunay as de
import Edge as ed
import Point as pt
import Triangle as tr
import math
import logging

class Teselation:

    logger = logging.getLogger('Teselation')

    '''Constructor de la clase, recibimos todos los triangulos posibles'''
    def __init__(self, triangles):
        self.triangles = triangles

    ''''''
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
                    self.logger.info('Intersection: {}'.format(inter_edge))
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
                cs = self.clean_segments(circle, e1, a,b,c)
                lines = lines + cs
                e1.set_bisector(cs[0])
                edges_triangles.remove(e1)
            if (e2 in edges_triangles):
                cs = self.clean_segments(circle, e2, b,c,a)
                lines = lines + cs
                e2.set_bisector(cs[0])
                edges_triangles.remove(e2)
            if (e3 in edges_triangles):
                cs = self.clean_segments(circle, e3, c,a,b)
                lines = lines + cs
                e3.set_bisector(cs[0])
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
        x0 = -a*c/(a*a+b*b)
        y0 = -b*c/(a*a+b*b)
        d = r*r - c*c/(a*a+b*b)
        mult = math.sqrt(d / (a*a+b*b));
        ax = x0 + b * mult;
        bx = x0 - b * mult;
        ay = y0 - a * mult;
        by = y0 + a * mult;
        self.logger.info('Intersection at: ({},{}) and ({},{})'.format(ax, ay, bx, by))


    '''Metodo auxiliar para calcular raices.'''
    def cuad(self, a,b,c):
        if (b != 0):
            return (-1 * (a/b), -1 * (c/b))
        else:
            return (-1 * a,-1 * c)

    '''Metodo para calcular las raices cuadradas de una ecuacion'''
    def chicharronera(self, a,b,c):
        sqr = math.sqrt(b**2 - (4 * a * c))
        res = -1 * b
        return ((res + sqr)/(2*a), (res - sqr)/(2*a))

    '''Metodo para dados un circulo y una linea, calcular sus puntos de interseccion.'''
    def inter_cl(self, circle, line):
        mid = line.p1.middle_point(line.p2)
        (a,b,c) = line.get_mediatrix() # ax + by + c = 0
        x, y, xs, ys, r = circle.get_equation_circ() # x2 + y2 + x + y + r = 0
        a,c = self.cuad(a,b,c) #ax/b + c/b
        x = x + (a**2)
        r = r + (c**2) + (c * ys)
        xs = xs + (2 * a * c) + (a * ys)#x
        x1, x2 = self.chicharronera(x,xs,r)
        y1 = a*x1 + c
        y2 = a*x2 + c
        p1 = pt.Point(x1, y1)
        p2 = pt.Point(x2, y2)
        return (p1, p2)

    '''Metodo que dados tres puntos, regresa dos aristas'''
    def draw_semi_lines(self, coord1, coord2, origin):
        return [ed.Edge(coord1, origin), ed.Edge(coord2, origin)]
