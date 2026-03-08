from datetime import datetime
import DelaunayBW as de
import Drawer as dr
import Edge as ed
import Point as pt
import Teselation as ts
import random
import Drawer as dr
import logging

class Board:

    '''Constructor, recibimos  los puntos  en txt. Probablemente  aqui sea
    buena idea  hacer la parte  de isometria, como lo  tenemos siempre
    calcula la isometria hasta que se pide.
    '''
    logger = logging.getLogger('Board')

    def __init__(self, pts):
        self.pts = pts
        self.iso_pts = self.__calculate_pts_iso()
        self.edges = []
        self.triangles = []
        self.logger.info('The points are: {}'.format(self.pts))
        self.logger.info('The iso_points are: {}'.format(self.iso_pts))

    '''ToString de la clase.'''
    def __str__(self):
        return str(pts)

    '''Actualizar los puntos en el tablero de processing.'''
    def update(self):
        for pti in self.iso_pts:
            pti.update()

    '''Metodo que  regresa los puntos tal  y como los leemos  del archivo,
    este es el encargado de regresar cosas cuando hacemos un reset.'''
    def get_pts_txt(self):
        return self.pts

    '''Metodo que "resetea" las  configuraciones iniciales del diagrama de
    voronoi y la triangulacion de delaunay usando los puntos iniciales.'''
    def reset(self):
        self.logger.info('Reset the board.')
        self.iso_pts = self.__calculate_pts_iso()
        delaunay = de.DelaunayBW(self.iso_pts)
        triangles = delaunay.get_triangulation()
        polygons = ts.Teselation(triangles)
        self.edges = polygons.process_intersection()
        self.logger.info('iso_pts: {}.'.format(self.iso_pts))
        return (self.iso_pts, self.edges, triangles)

    '''Metodo que  dibuja los puntos,  depende de si se  van a mover  o no
    todos. Todos son azules (ver Pt.py),  si solo uno se mueve, ese es
    guinda.'''
    def drawPoints(self):
        for pti in self.iso_pts:
            pti.draw()
        return self.iso_pts

    '''Metodo  que  dibuja las  lineas  (aristas),  calculamos las  medias
    aristas del  diagrama de Voronoi  y las  aristas de los  triangulos de
    delaunay, de colorearlas se encarga Triangle.py y Edge.py'''
    def drawLines(self):
        stroke(255,0,0)
        print('(Aqui deberiamos meter la actualizacion del paper)')
        delaunay = de.DelaunayBW(self.iso_pts)
        self.triangles = delaunay.get_triangulation()
        polygons = ts.Teselation(self.triangles)
        self.edges = polygons.process_intersection()
        for p1p2 in self.edges:
            p1p2.draw()
        self.logger.info('Triangles to draw: {}.'.format(self.triangles))
        for t in self.triangles:
            t.draw()
        return self.edges

    '''Metodo que calcula los puntos cambiados con la isometria.'''
    def __calculate_pts_iso(self):
        def g(p):
            return (p*50)
        def f(p):
            return (g(p.x), g(p.y), p.m, p.flag)
        board = list(map(lambda x: f(x), self.pts))
        pts = []
        for b in board:
            if b[3]:
                new_b = b[1] - (b[2] * b[0])
                pts.append(pt.Point(b[0], b[1], b[2], new_b))
            else:
                pts.append(pt.Point(b[0], b[1], flag=False))

        return pts

    '''Metodo que calcula los puntos cambiados con la isometria.'''
    def __calculate_new_iso(self, pts):
        def f(t):
            return (t[0]-50, t[1]+50)
        board = list(map(lambda x: f(x), pts))
        return board

    '''Metodo que regresa los puntos isometricos.'''
    def get_pts_iso(self):
        return self.iso_pts

    '''Metodo  que   regresa  las   aristas  iniciales  para   la  primera
    configuracion de las aristas de voronoi'''
    def get_vor_edges(self):
        delaunay = de.DelaunayBW(self.iso_pts)
        triangles = delaunay.get_triangulation()
        polygons = ts.Teselation(triangles)
        self.edges = polygons.process_intersection()
        return self.edges

    '''Metodo para escribir en un archivo de LaTeX la configuracion de
    los puntos en tikz y poder exportarlos como imagen a un archivo de LaTeX.'''
    def print_thesis_in_tikz(self):
        self.logger.info('Tikz saved on: {}.'.format('tikz.tex'))
        tikz = dr.Drawer(self.edges, self.triangles)
        string = tikz.tikz()
        with open("../tikz.tex", "a") as f:
            f.write(string)

    '''save frame at: examples/stored/d-m-h:m:s.tes'''
    def save_thesis(self):
        now = datetime.now()
        current = now.strftime('%d-%m-%H:%M:%S')
        file_name = '../examples/stored/{}.tes'.format(str(current))
        self.logger.info('Save frame at {}.'.format(file_name))
        f = open(file_name, 'w')
        time = self.iso_pts[0].current
        for nb in self.pts:
            if nb.flag:
                s = '{}\t{}\t{}\t{}\n'.format(nb.x, nb.y, nb.m, nb.b)
            else:
                s = '{}\t{}# static point\n'.format(nb.x, nb.y)
            f.write(s)
        f.close()
