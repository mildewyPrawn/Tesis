import Circle as cr
import math

class Point:
    x = 0.0
    y = 0.0

    '''Constructor de la  clase, inicializa las coordenadas de  un punto y
    un nombre'''
    def __init__(self, x, y, n=''):
        self.x = x
        self.y = y
        self.n = n


    '''toString de la clase.'''
    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    '''So se can get by index a point.'''
    def __getitem__(self, key):
        return self.x if key == 0 else self.y

    # '''equals de la clase.'''
    # def __eq__(self, pt):
    #     return (self.x == pt.x and self.y == pt.y)

    def is_between(self, p1, p2):
        # p1 = edge.p1
        # p2 = edge.p2
        cross_product = self.ccw(p1, p2)
        if (abs(cross_product) > 0):
            return False
        dot_product = (p2.x - self.x) * (p1.x - self.x) + (p2.y - self.y)*(p1.y - self.y)
        if (dot_product < 0):
            return False
        squared_length = (p1.x - self.x)*(p1.x - self.x) + (p1.y - self.y)*(p1.y - self.y)
        if (dot_product > squared_length):
            return False
        return True

    '''Metodo que regresa una lista con la posicion en forma de lista.'''
    def pos(self):
        return [self.x, self.y]

    '''Metodo que nos dice si dos puntos son o no iguales.'''
    def is_equal(self, point):
        return (self.x == point.x and self.y == point.y)

    '''Counterclockwise  turns.   Given  three  points  self,  b,  and  c,
    determine  whether  they  form   a  counterclockwise  angle.   The
    function ccw takes two Point inputs  self, b, and c and returns +1
    if self->b->c is  a counterclockwise angle, -1 if  self->b->c is a
    clockwise angle, and 0 if self->b->c are collinear.'''
    def ccw(self, b,c):
        ax = self.x
        ay = self.y
        return (b.x - ax) * (c.y - ay) - (c.x - ax) * (b.y - ay)

    '''Nos regresa la distancia entre self y pt.'''
    def distance(self, pt):
        x = pt.x
        y = pt.y
        d = math.sqrt(((self.x - x)**2) + ((self.y - y)**2))
        return d

    '''Nos dice  si un punto (self),  esta dentro de un  circulo (definido
    por centro (x0, y0) de radio r)'''
    def inside(self, circ):
        # pt = Point(x0, y0)
        pt = circ.origin
        d = self.distance(pt)
        return d < circ.radius

    def middle_point(self, pt):
        x = (self.x + pt.x)/2
        y = (self.y + pt.y)/2
        return Point(x,y)

    '''Metodo que dibuja el punto en processing'''
    def draw(self, flag=True):
        if flag:
            stroke(0, 0, 255)
            fill(0,0,255)
        else:
            stroke(0,255,255)
            fill(0,255,255)
        ellipse(self.x, self.y, 5, 5)
