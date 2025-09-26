import math

import Point as pt
import Edge as ed

class Triangle:

    circle = None

    '''Constructor de  la clase,  recibe tres puntos  y si  son distintos,
    crea un tringulo, ademas creamos las aristas'''
    def __init__(self, a, b, c):
        if a is not b and a is not c:
            self.a = a
        if b is not a and b is not c:
            self.b = b
        if c is not a and c is not b:
            self.c = c
        self.ed1 = ed.Edge(self.a, self.b)
        self.ed2 = ed.Edge(self.b, self.c)
        self.ed3 = ed.Edge(self.c, self.a)
        self.circumcircle()

    '''toString de la clase'''
    def __repr__(self):
        return '[{}, {}, {}]'.format(self.ed1.p1, self.ed2.p1, self.ed3.p1)
        # return

    def __eq__(self, tri):
        if (tri == None):
            return False
        return (self.a == tri.a or self.a == tri.b or self.a == tri.c) and (self.b == tri.a or self.b == tri.b or self.b == tri.c) and (self.c == tri.a or self.c == tri.b or self.c == tri.c)

    def intersect(self, tri):
        t1a = self.ed1
        t1b = self.ed2
        t1c = self.ed3
        t2a = tri.ed1
        t2b = tri.ed2
        t2c = tri.ed3
        t1 = [t1a, t1b, t1c]
        t2 = [t2a, t2b, t2c]
        for t1i in t1:
            for t2i in t2:
                if (t1i == t2i):
                    return t1i
        return None

    '''Metodo que dados dos triangulos nos dice si son o no iguales.'''
    def is_equal(self, tri):
        return (self.a is tri.a or self.a is tri.b or self.a is tri.c) and (self.b is tri.a or self.b is tri.b or self.b is tri.c) and (self.c is tri.a or self.c is tri.b or self.c is tri.c)

    '''Setter para circulo.'''
    def create_circle(self, c):
        self.circle = c

    '''Metodo que dibuja un triangulo  en processing. Manda a dibujar cada
    arista por separado (ver Edge.py)'''
    def draw(self):
        self.ed1.draw(2)
        self.ed2.draw(2)
        self.ed3.draw(2)
        self.circle.draw()


    def inCircumcircle(self, pt):
        dx = self.origin.x - pt.x
        dy = self.origin.y - pt.y
        return math.sqrt((dx  * dx)  + (dy * dy)) <= self.radius

    '''Dados tres  puntos nos  da la circunferencia  (origen y  radio) del
    circulo
    https://math.stackexchange.com/questions/213658/get-the-equation-of-a-circle-when-given-3-points
    Joseph O'Rourke Computational geometry in C makes without determinant'''
    def circumcircle(self):
        ax = self.a.x
        ay = self.a.y
        bx = self.b.x
        by = self.b.y
        cx = self.c.x
        cy = self.c.y
        axy = (ax**2) + (ay**2)
        bxy = (bx**2) + (by**2)
        cxy = (cx**2) + (cy**2)

        d = self.determinant_3x3(ax, ay, 1, bx, by, 1, cx, cy, 1)
        xd = self.determinant_3x3(axy, ay, 1, bxy, by, 1, cxy, cy, 1)
        yd = self.determinant_3x3(axy, ax, 1, bxy, bx, 1, cxy, cx, 1)

        x0 = 0.5 * (xd / d)  # x of the circle
        y0 = -0.5 * (yd / d) # y of the circle

        # origin
        self.origin = pt.Point(x0, y0)
        rd = self.determinant_3x3(axy, ax, ay, bxy, bx, by, cxy, cx, cy)

        # radius
        self.radius = self.a.distance(self.origin) # radius of the circle

        # self.tangent = x0 + self.radius # tangente del circulo sobre x (Fortune)
        return (self.origin, self.radius)

    '''
    |e f|
    |h i|
    '''
    def determinant_2x2(self, e, f, h, i):
        return (e * i) - (f * h)

    '''
    |ax ay az|
    |bx by bz|
    |cx cy cz|
    '''
    def determinant_3x3(self, ax, ay, az, bx, by, bz, cx, cy, cz):
        return (ax * self.determinant_2x2(by, bz, cy, cz)) - (ay * self.determinant_2x2(bx, bz, cx, cz)) + (az * self.determinant_2x2(bx, by, cx, cy))
