import Point as pt
import math

class Circle:

    '''Constructor de la clase, podemos crear circulos dados tres puntos o
    dado su origen y su radio'''
    def __init__(self, xy=None, r=0, a=None, b=None, c=None):
        self.origin = xy
        self.radius = r
        self.a = a
        self.b = b
        self.c = c

    '''toString de la clase'''
    def __str__(self):
        return '{} at {} coll {}{}{}'.format(self.origin, self.radius, self.a, self.b, self.c)

    '''Dados tres  puntos nos  da la circunferencia  (origen y  radio) del
    circulo
    https://math.stackexchange.com/questions/213658/get-the-equation-of-a-circle-when-given-3-points'''
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

        self.origin = pt.Point(x0, y0)

        rd = self.determinant_3x3(axy, ax, ay, bxy, bx, by, cxy, cx, cy)

        self.radius = self.a.distance(self.origin) # radius of the circle
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

    '''Metodo que dibuja el circulo en processing'''
    def draw(self):
        noFill()
        stroke(255, 204, 0)
        circle(self.origin.x, self.origin.y, self.radius*2);
