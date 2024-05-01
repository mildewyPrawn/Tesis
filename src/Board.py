import random
import Point as pt
import Edge as ed
import Delaunay as de
import Teselation as ts
import Drawer as dr

class Board:

    '''Constructor, recibimos  los puntos  en txt. Probablemente  aqui sea
    buena idea  hacer la parte  de isometria, como lo  tenemos siempre
    calcula la isometria hasta que se pide.
    '''
    def __init__(self, pts, rand):
        self.pts = pts
        self.iso_pts = self.__calculate_pts_iso()
        self.edges = []
        self.triangles = []
        # Random for 1 or all points
        self.rand = rand
        print('pts: {}'.format(self.pts))
        print('begin iso_pts')
        for p in self.iso_pts:
            print('iso: {}'.format(p))
        print('end iso_pts')

    '''ToString de la clase.'''
    def __str__(self):
        return str(pts)

    '''Metodo que hace que un  punto se mueva "aleatoriamente", depende de
    si se  van a  mover todos o  no (bandera rand),  vamos a  tomar un
    punto y calcular dos valores  aleatorios, si estos son congruentes
    con 0 modulo  2, entonces los movemos con 50  pixeles a la derecha
    y/o para abajo.'''
    def randomize(self): #TODO no caer en el mismo punto
        new_iso = []
        r = int(random.uniform(0,100))
        rx = int(random.uniform(0,100))
        ry = int(random.uniform(0,100))
        if self.rand:
            pti = self.iso_pts[0]
            x = pti.x
            y = pti.y
            rx = int(random.uniform(0,100))
            ry = int(random.uniform(0,100))
            if rx % 2 == 0:
                x = x + 50
            if ry % 3 == 0:
                y = y + 50
            new_iso.append((pt.Point(x,y)))
            for i in range(1, len(self.iso_pts)):
                new_iso.append(self.iso_pts[i])
        else: # movemos todos los puntos
            for pti in self.iso_pts:
                rx = int(random.uniform(0,100))
                ry = int(random.uniform(0,100))
                x = pti.x
                y = pti.y
                if r % 2 == 0:
                    if rx % 2 == 0:
                        x = x + 50
                    else:
                        x = x - 10
                    if ry % 3 == 0:
                        y = y + 50
                    else:
                            y = y - 10
                new_iso.append(pt.Point(x,y))
        self.iso_pts = new_iso

    '''Metodo que  regresa los puntos tal  y como los leemos  del archivo,
    este es el encargado de regresar cosas cuando hacemos un reset.'''
    def get_pts_txt(self):
        return self.pts

    '''Metodo que "resetea" las  configuraciones iniciales del diagrama de
    voronoi y la triangulacion de delaunay usando los puntos iniciales.'''
    def reset(self):
        print('reset program')
        self.iso_pts = self.__calculate_pts_iso()
        delaunay = de.Delaunay(self.iso_pts)
        triangles = delaunay.get_triangulation()
        polygons = ts.Teselation(triangles)
        self.edges = polygons.process_intersection()
        print('begin reset')
        for p in self.iso_pts:
            print('iso: {}'.format(p))
        print('end reset')
        return (self.iso_pts, self.edges, triangles)

    '''Metodo que  dibuja los puntos,  depende de si se  van a mover  o no
    todos. Todos son azules (ver Pt.py),  si solo uno se mueve, ese es
    guinda.'''
    def drawPoints(self):
        if self.rand:
            self.iso_pts[0].draw(False)
            for i in range(1, len(self.iso_pts)):
                self.iso_pts[i].draw()
        else:
            for pti in self.iso_pts:
                pti.draw()
        return self.iso_pts

    '''Metodo  que  dibuja las  lineas  (aristas),  calculamos las  medias
    aristas del  diagrama de Voronoi  y las  aristas de los  triangulos de
    delaunay, de colorearlas se encarga Triangle.py y Edge.py'''
    def drawLines(self):
        stroke(255,0,0)
        print('(Aqui deberiamos meter la actualizacion del paper)')
        delaunay = de.Delaunay(self.iso_pts)
        self.triangles = delaunay.get_triangulation()
        polygons = ts.Teselation(self.triangles)
        self.edges = polygons.process_intersection()
        for p1p2 in self.edges:
            p1p2.draw()
        print('\tdrawLines (in B.py call from T.py)')
        for ti in self.triangles:
            print('DT(i): {}'.format(ti))
        for t in self.triangles:
            t.draw()
        return self.edges

    '''Metodo que calcula los puntos cambiados con la isometria.'''
    def __calculate_pts_iso(self):
        def f(t):
            return ((t[0]*100)+250, (t[1]*100)+250)
        def g(t):
            return ((t[0]-250)/100, (t[1]-250)/100)
        board = list(map(lambda x: f(x), self.pts))
        pts = []
        for b in board:
            pts.append(pt.Point(b[0], b[1]))
        pts.sort(key=lambda pt: pt.x)
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
        delaunay = de.Delaunay(self.iso_pts)
        triangles = delaunay.get_triangulation()
        polygons = ts.Teselation(triangles)
        self.edges = polygons.process_intersection()
        return self.edges

    def print_tesis_in_tikz(self):
        tikz = dr.Drawer(self.edges, self.triangles)
        string = tikz.tikz()
        print(string)
