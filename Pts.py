class Pts:

    '''Constructor, recibimos  los puntos  en txt. Probablemente  aqui sea
    buena idea  hacer la parte  de isometria, como lo  tenemos siempre
    calcula la isometria hasta que se pide.

    '''
    def __init__(self, pts):
        self.pts = pts
        self.iso_pts = self.__calculate_pts_iso()

    '''ToString de la clase.'''
    def __str__(self):
        return str(pts)

    '''Metodo de prueba.'''
    def hola(self):
        print("holap")

    '''Metodo que  regresa los puntos tal  y como los leemos  del archivo,
    este es el encargado de regresar cosas cuando hacemos un reset.'''
    def get_pts_txt(self):
        return self.pts

    '''Metodo que calcula los puntos cambiados con la isometria.'''
    def __calculate_pts_iso(self):
        def f(t):
            return ((t[0]*100)+250, (t[1]*100)+250)
        board = list(map(lambda x: f(x), self.pts))
        print(board)
        return board

    '''Metodo que regresa los puntos isometricos.'''
    def get_pts_iso(self):
        return self.iso_pts
