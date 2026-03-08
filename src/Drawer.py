import Circle as cr
import Delaunay as de
import Edge as ed
import Point as pt
import Triangle as tr
import math
import logging

class Drawer:

    logger = logging.getLogger('Drawer')

    '''Constructor  que  recibe  los  triangulos de  la  triangulacion  de
    Delaunay y las aristas del diagrama de voronoi'''
    def __init__(self, edges, triangles):
        self.edges = edges
        self.triangles = triangles

    '''Metodo para calcular los limites de processing.'''
    def min_max(self, pts):
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        for pt in pts:
            x = pt.x
            y = pt.y
            if (x < min_x):
                min_x = x
            if (x > max_x):
                max_x = x
            if (y < min_y):
                min_y = y
            if (y > max_y):
                max_y = y
        return ((min_x/100, min_y/100), (max_x/100, max_y/100))

    '''Funcion que se encarga de  dibujar vertices, aristas (de triangulos
    y del diagrama), y circurlos'''
    def tikz(self):
        begin = '\\begin{tikzpicture}[scale=1.5,thick, every node/.style={scale=1}]\n'
        end = '\\end{tikzpicture}\n'
        voronoi = '\\draw [line width=0.35mm, green] ({}, {}) -- ({},{});\n'
        voronoio = '\\draw [dashed, green] ({}, {}) -- ({},{});\n'
        delaunay = '\\draw [line width=0.35mm ,red] ({}, {}) --({}, {});\n'
        #point = '\\filldraw[blue] ({},{}) circle (1pt) node[anchor=south] {{}};\n'
        point = '\\filldraw[{}] ({},{}) circle (1pt) node[anchor=south] {{}};\n'
        circle = '\\filldraw [yellow, fill=none] ({},{}) circle ({});\n'
        limit = '\\draw [line width=0.35mm, green] ({}, {}) -- ({},{});\n'
        tikz = begin
        edges_triangles = set()
        all_pts = set()
        pts = set()

        # draw red triangles
        # add blue points (pts)
        # draw yellow circles

        tikz = begin
        for e in self.edges:
            tikz = tikz + voronoi.format(e.p1.x/100, e.p1.y/100, e.p2.x/100, e.p2.y/100)

        for t in self.triangles:
            e1 = t.ed1
            e2 = t.ed2
            e3 = t.ed3
            a = t.a
            b = t.b
            c = t.c
            pts.add(a)
            pts.add(b)
            pts.add(c)
            all_pts.add(a)
            all_pts.add(b)
            all_pts.add(c)
            c1 = cr.Circle(a=t.a, b=t.b, c=t.c)
            (o, r) = c1.circumcircle()
            tikz = tikz + circle.format(o.x/100, o.y/100, r/100)
            tikz = tikz + delaunay.format(e1.p1.x/100, e1.p1.y/100, e1.p2.x/100, e1.p2.y/100)
            tikz = tikz + delaunay.format(e2.p1.x/100, e2.p1.y/100, e2.p2.x/100, e2.p2.y/100)
            tikz = tikz + delaunay.format(e3.p1.x/100, e3.p1.y/100, e3.p2.x/100, e3.p2.y/100)

        # draw green lines (voronoi lines)  that are not in the convex
        # hull
        for i in range(0, len(self.triangles)):
            for j in range(i+1, len(self.triangles)):
                t1 = self.triangles[i]
                t2 = self.triangles[j]
                edges_triangles.add(t1.ed1)
                edges_triangles.add(t1.ed2)
                edges_triangles.add(t1.ed3)
                edges_triangles.add(t2.ed1)
                edges_triangles.add(t2.ed2)
                edges_triangles.add(t2.ed3)
                c1 = cr.Circle(a=t1.a, b=t1.b, c=t1.c)
                c2 = cr.Circle(a=t2.a, b=t2.b, c=t2.c)
                (o1, _) = c1.circumcircle()
                (o2, _) = c2.circumcircle()
                inter_edge = t1.intersect(t2)
                if (inter_edge != None and inter_edge in edges_triangles):
                    edges_triangles.remove(inter_edge)
                    all_pts.add(o1)
                    all_pts.add(o2)
                    e = ed.Edge(o1, o2)
                    f = ed.Edge(o2, o1)
                    if (e in self.edges):
                        self.edges.remove(e)
                    tikz = tikz + voronoi.format(o1.x/100, o1.y/100, o2.x/100, o2.y/100)

        # add more points
        for line in self.edges:
            xp1 = line.p1
            yp1 = line.p1
            xp2 = line.p2
            yp2 = line.p2
            all_pts.add(line.p1)
            all_pts.add(line.p2)

        # get max and min coords
        (min_, max_) = self.min_max(all_pts)
        e1 = ed.Edge(pt.Point(min_[0], min_[1]), pt.Point(max_[0], min_[1]))
        e2 = ed.Edge(pt.Point(min_[0], min_[1]), pt.Point(min_[0], max_[1]))
        e3 = ed.Edge(pt.Point(max_[0], max_[1]), pt.Point(min_[0], max_[1]))
        e4 = ed.Edge(pt.Point(max_[0], max_[1]), pt.Point(max_[0], min_[1]))

        self.logger.info('Max coords are: {}, {}, {}, {}'.format(e1, e2, e3, e4))

        # draw blue points for triangle vertices
        for t in self.triangles:
            e1 = t.ed1
            e2 = t.ed2
            e3 = t.ed3
            e1p1 = e1.p1
            e1p2 = e1.p2
            e2p1 = e2.p1
            e2p2 = e2.p2
            e3p1 = e3.p1
            e3p2 = e3.p2

            tikz = tikz + point.format("blue", e1p1.x/100, e1p1.y/100)
            tikz = tikz + point.format("blue", e1p2.x/100, e1p2.y/100)
            tikz = tikz + point.format("blue", e2p1.x/100, e2p1.y/100)
            tikz = tikz + point.format("blue", e2p2.x/100, e2p2.y/100)
            tikz = tikz + point.format("blue", e3p1.x/100, e3p1.y/100)
            tikz = tikz + point.format("blue", e3p2.x/100, e3p2.y/100)

        tikz = tikz + end

        return tikz
