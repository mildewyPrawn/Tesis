import Circle as cr
import Delaunay as de
import Edge as ed
import Point as pt
import Triangle as tr
import math

class Drawer:

    '''Constructor  que  recibe  los  triangulos de  la  triangulacion  de
    Delaunay y las aristas del diagrama de voronoi'''
    def __init__(self, edges, triangles):
        self.edges = edges
        self.triangles = triangles

    '''Funcion que se encarga de  dibujar vertices, aristas (de triangulos
    y del diagrama), y circurlos'''
    def tikz(self):
        begin = '\\begin{tikzpicture}[scale=1.5,thick, every node/.style={scale=1}]\n'
        end = '\\end{tikzpicture}\n'
        voronoi = '\\draw [line width=0.35mm, green] ({}, {}) -- ({},{});\n'
        delaunay = '\\draw [line width=0.35mm ,red] ({}, {}) --({}, {});\n'
        point = '\\filldraw[blue] ({},{}) circle (1pt) node[anchor=south] {{}};\n'
        circle = '\\filldraw [yellow, fill=none] ({},{}) circle ({});\n'
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
            tikz = tikz + delaunay.format(e1.p1.x/100, e1.p1.y/100, e1.p2.x/100, e1.p2.y/100)
            tikz = tikz + delaunay.format(e2.p1.x/100, e2.p1.y/100, e2.p2.x/100, e2.p2.y/100)
            tikz = tikz + delaunay.format(e3.p1.x/100, e3.p1.y/100, e3.p2.x/100, e3.p2.y/100)
            circ = cr.Circle(a=a, b=b, c=c)
            (o, r) = circ.circumcircle()
            tikz = tikz + circle.format(o.x/100, o.y/100, r/100)
        for e in self.edges:
            tikz = tikz + point.format(e.p1.x/100, e.p1.y/100)
        tikz = tikz + end
        return tikz
