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

    '''toString de la clase'''
    def __str__(self):
        return 'A:{}-B:{}-C:{}'.format(self.ed1, self.ed2, self.ed3)
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
