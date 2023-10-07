import Triangle as tr
import Circle as cr
import Point as pt

class Delaunay:

    '''Constructor de la clase, recibimos  los puntos y los ordenamos para
    calcular la triangulacion, recibimos los puntos ya ordenados.

    '''
    def __init__(self, pts):
        self.pts = pts
        self.delaunay()

    '''toString de la clase (puntos y triangulos).'''
    def __str__(self):
        return '[{}], [{}]'.format(self.pts, self.triangulation)

    '''Funcion para obtener la triangulacion.'''
    def get_triangulation(self):
        return self.triangulation

    '''Funcion para obtener los puntos.'''
    def get_points(self):
        return self.pts

    '''Funcion  para  calcular  la  triangulacion de  Delaunay  dados  los
    puntos. La calculamos en O(n3) "para todos los puntos pqr..."'''
    def delaunay(self):
        ts = []
        for p in self.pts:
            for q in self.pts:
                for r in self.pts:
                    if p.ccw(q,r) > 0:
                        ts.append(tr.Triangle(p,q,r))

        self.filter_good_tris(ts)

    '''Funcion  auxiliar  para una  vez  que  tenemos todos  los  posibles
    triangulos eliminar los que no son de Delaunay'''
    def filter_good_tris(self, ts):
        good_tris = []
        for tri in ts:
            circle = cr.Circle(a=tri.a, b=tri.b, c=tri.c)
            circle.circumcircle()
            x0y0, r = circle.origin, circle.radius
            valid = True
            for pt in self.pts:
                if pt.inside(circle):
                    valid = False
                    break
            if valid:
                tri.create_circle(circle)
                good_tris.append(tri)
        self.filter_repeat(good_tris)

    '''Funcion  auxiliar para  una  vez que  tenemos  puros triangulos  de
    Delaunay, eliminar  los repetidos.  El triangulo  ABC es  igual al
    CAB, etc'''
    def filter_repeat(self, tris):
        good_tris = []
        [good_tris.append(x) for x in tris if x not in good_tris]
        self.triangulation = good_tris
