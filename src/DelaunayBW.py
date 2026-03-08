import math

import Point as pt
import Edge as ed
import Triangle as tr
import Circle as cr
import logging

class DelaunayBW:

    logger = logging.getLogger('Delaunay')

    '''Constructor de la clase, verificamos  que la nube de puntos sea
    triangulable  (mayor  o igual  a  3  puntos), e  inicializamos  el
    outer_triangle que envuelve a la nube de puntos.'''
    def __init__(self, pts):
        if (len(pts) < 3):
            raise Exception("The number of points needs to be at least three, you have: {}".format(len(pts)))
        self.pts = pts
        self.outer_triangle = self.outer_triangle(pts)
        self.logger.info('The points are: {}'.format(self.pts))
        self.logger.info('Creating the Outer Triangle: {}'.format(self.outer_triangle))
        self.triangulate()

    '''getter para regresar la triangulacion'''
    def get_triangulation(self):
        return self.triangulation

    '''Metodo para calcular el outer_triangle, que es un triangulo que
    envuelve a todos los puntos de la nube de puntos.'''
    def outer_triangle(self, pts):
        minx = float('inf')
        miny = float('inf')
        maxx = float('-inf')
        maxy = float('-inf')

        for pti in pts:
            minx = min(minx, pti.x)
            miny = min(miny, pti.y)
            maxx = max(maxx, pti.x)
            maxy = max(maxy, pti.y)

        dx = (maxx - minx) * 10
        dy = (maxy - miny) * 10

        p0 = pt.Point(minx - dx, miny - dy * 3)
        p1 = pt.Point(minx - dx, maxy + dy)
        p2 = pt.Point(maxx + dx * 3, maxy + dy)

        return tr.Triangle(p0, p1, p2)

    '''Metodo  para calcular  la triangulacion  de delauay,  para cada
    punto, lo agregamos  a una triangulacion valida  y verificamos que
    siga siendo valida, en caso  contrario quitamos aristas. El metodo
    supone que la  triangulacion inicia con el  outer_triangle, por lo
    que al  final quitamos  las aristas conectadas  a los  vertices de
    este triangulo'''
    def triangulate(self):
        triangles = [self.outer_triangle]

        for pt in self.pts:
            triangles = self.add_vertex(pt, triangles)

            def __bounding_with_outer(self, triangle):
                ot = self.outer_triangle
                flag = not (triangle.a == ot.a or triangle.a == ot.b or triangle.a == ot.c or triangle.b == ot.a or triangle.b == ot.b or triangle.b == ot.c or triangle.c == ot.a or triangle.c == ot.b or triangle.c == ot.c)
                return flag

        triangles = list(filter(lambda x : __bounding_with_outer(self, x), triangles))

        for tri in triangles:
            circle = cr.Circle(a=tri.a, b=tri.b, c=tri.c)
            circle.circumcircle()
            x0y0, r = circle.origin, circle.radius
            tri.create_circle(circle)

        self.triangulation = triangles

    def __retriangulate(self, pts_to_retriangulate):
        triangles = [self.outer_triangle]

        for pt in pts_to_retriangulate:
            triangles = self.add_vertex(pt, triangles)

            def __bounding_with_outer(self, triangle):
                ot = self.outer_triangle
                flag = not (triangle.a == ot.a or triangle.a == ot.b or triangle.a == ot.c or triangle.b == ot.a or triangle.b == ot.b or triangle.b == ot.c or triangle.c == ot.a or triangle.c == ot.b or triangle.c == ot.c)
                return flag

        triangles = list(filter(lambda x : __bounding_with_outer(self, x), triangles))

        for tri in triangles:
            circle = cr.Circle(a=tri.a, b=tri.b, c=tri.c)
            circle.circumcircle()
            x0y0, r = circle.origin, circle.radius
            tri.create_circle(circle)

        return triangles


    '''Metodo que agrega  un vertice a una  triangulacion valida, cada
    que  se  agrega  se  verifica sobre  las  circunferencias  que  lo
    contienen  y se  cambian  las aristas  necesarias  para hacer  una
    triangulacion de Delaunay valida.'''
    def add_vertex(self, point, triangles):
        def __filter_triangles(self):
            new_triangles = []
            edges = []
            for tr in triangles:
                if (tr.inCircumcircle(point)):
                    edges.append(ed.Edge(tr.a, tr.b))
                    edges.append(ed.Edge(tr.b, tr.c))
                    edges.append(ed.Edge(tr.c, tr.a))
                else:
                    new_triangles.append(tr)

            return (new_triangles, edges)

        triangles, edges = __filter_triangles(self)
        edges = self.unique_edges(edges)

        for edg in edges:
            triangles.append(tr.Triangle(edg.p1, edg.p2, point))

        return triangles

    '''Metodo auxiliar para remover aristas duplicadas (a-b) o (b-a).'''
    def unique_edges(self, edges):
        unique = []

        for i in range(len(edges)):
            is_unique = True
            for j in range(len(edges)):
                if (i != j and edges[i].is_equal(edges[j])):
                    is_unique = False
                    break
            if is_unique:
                unique.append(edges[i])

        return unique

    '''doesn't work'''
    def update(self, new_pt):
        pts_to_retriangulate = []
        good_triangles = []
        for t in self.triangulation:
            if new_pt in t:
                pts_to_retriangulate.append(t.a)
                pts_to_retriangulate.append(t.b)
                pts_to_retriangulate.append(t.c)
            else:
                good_triangles.append(t)
        new_triangles = self.__retriangulate(pts_to_retriangulate)

        good_triangles.extend(new_triangles)

        self.triangulation = good_triangles
        return self.triangulation

