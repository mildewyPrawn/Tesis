import math
import Point as pt

class Edge:

    '''Constructor  de la  clase,  recibe dos  puntos y  si  estos no  son
    iguales, creamos la arista.'''
    def __init__(self, p1, p2):
        if p1 is not p2:
            self.p1 = p1
            self.p2 = p2

    '''toString de la clase.'''
    def __str__(self):
        return '{}-{}[{}]'.format(self.p1, self.p2, self.slope)

    def __eq__(self, edge):
        if (edge == None):
            return False
        return (self.p1.is_equal(edge.p1) or self.p2.is_equal(edge.p1)) and (self.p1.is_equal(edge.p2) or self.p2.is_equal(edge.p2))

    def __key(self):
        return (self.p1, self.p2)

    def __u_key(self):
        return (self.p2, self.p1)

    def __hash__(self):
        return hash(self.__key()) & hash(self.__u_key())

    def p1(self):
        return self.p1

    def touch(self, edge):
        return self.p1 == edge.p1 or self.p1 == edge.p2 or self.p2 == edge.p1 or self.p2 == edge.p2

    def invert(self):
        e = Edge(self.p2, self.p1)
        return e

    '''Metodo para verificar si dos aristas son o no iguales.'''
    def is_equal(self, edge):
        return (self.p1.is_equal(edge.p1) or self.p2.is_equal(edge.p1)) and (self.p1.is_equal(edge.p2) or self.p2.is_equal(edge.p2)) or self == edge

    '''Metodo para calcular la distancia de una arista (entre sus puntos).'''
    def length(self):
        return math.sqrt(math.pow(self.p2.pos()[0] - self.p1.pos()[0],2) + math.pow(self.p2.pos()[1] - self.p1.pos()[1],2))

    '''Metodo para ver si dos aristas se intersectan o no.'''
    def edge_intersection(self, edge):
        if self.is_equal(edge):
            return False
        else:
            try:
                x1 = self.p1.pos()[0]
                x2 = self.p2.pos()[0]
                x3 = edge.p1.pos()[0]
                x4 = edge.p2.pos()[0]
                y1 = self.p1.pos()[1]
                y2 = self.p2.pos()[1]
                y3 = edge.p1.pos()[1]
                y4 = edge.p2.pos()[1]
                t = (((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4))) / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
                u = (((x2 - x1) * (y1 - y3)) - ((y2 - y1) * (x1 - x3))) / (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
                if (t >= 0 and t <= 1) and (u >= 0 and u <= 1):
                    x = int(x1 + t*(x2 - x1))
                    y = int(y1 + t*(y2 - y1))
                    point = pt.Point(x, y)
                    if self.p1.is_equal(point) or self.p2.is_equal(point) or edge.p1.is_equal(point) or edge.p2.is_equal(point):
                        return False
                    else:
                        return True
                else:
                    return False
            except:
                return False

    '''Metodo para dibujar la arista en processing'''
    def draw(self, arg=1):
        if arg == 1: # voronoi diagram
            stroke(0, 255, 0)
        elif arg == 2: # delaunay triangulation
            stroke(255, 0, 0)
        else: # other edges
            stroke(0, 0, 255)
            # stroke(92.2, 0, 79.2)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
