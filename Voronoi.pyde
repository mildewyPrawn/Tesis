import random
import os
from Tesis import *
from Pts import *

MODE = "RANDOM" # RANDOM or USER
THREAD = "OFF" # ON or OFF
PEN = "DRAW" # DRAW or ERASER
FRAMERATE = 200

# with this i read files
file = os.environ['FILE']
with open(file) as f:
    lines = f.readlines()
points = lines_to_tuples(lines)

# TODO: crear un objeto
pts = Pts(points)

'''Metodo que necesita processing  para inicializar todo, asignamos el
tamano  de la  ventana  y el  background. points  son  los puntos  que
leemos.

Hasta ahorita solo usamos b, b2 (este no tanto)'''
def setup():
    global b, b2, points
    if MODE == "RANDOM":
        b, b2 = makeBoards(pts)
    size(700, 700)
    background(0)
    frameRate(FRAMERATE)

'''Metodo para poder  presionar teclas, de momento solo  está la tecla
de  reset que  será  para  rehacer todo  el  programa  con los  puntos
dados.'''
def keyPressed():
    global THREAD
    if key == " ":
        if THREAD == "OFF":
            THREAD = "ON"
        else:
            THREAD = "OFF"
    elif key == "r":
        reset()

'''Metodo reset,  servira para volver  a empeazar le ejecucion  con la
configuracion inicial.'''
def reset():
    global THREAD, b, b2, bInert
    THREAD = "OFF"
    b, b2 = makeBoards(pts)

'''Método para  dibujar, es  el main,  lo que  hace es  inicializar el
board y posteriormente, va a ir actualizandolo con los movimientos.'''
def draw():
    showBoard(b)
    # if THREAD == "ON":
        # updateBoard(b, b2, bInert)
