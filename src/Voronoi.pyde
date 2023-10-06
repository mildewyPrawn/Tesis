import random
import os
from Tesis import *
from Board import *
import Fortune as f

MODE = "RANDOM" # RANDOM or USER
THREAD = "OFF" # ON or OFF
PEN = "DRAW" # DRAW or ERASER
FRAMERATE = 1

# with this i read files
file = os.environ['FILE']
# argument for randomize 1 or all the points
argR = os.environ['R']
with open(file) as f:
    lines = f.readlines()
points = lines_to_tuples(lines)

pts = Board(points, argR == 'True')

'''Metodo que necesita processing  para inicializar todo, asignamos el
tamano  de la  ventana  y el  background. points  son  los puntos  que
leemos.'''
def setup():
    global p, e, points
    if MODE == "RANDOM":
        p, e = makeBoards(pts)
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
    global THREAD, p, e, bInert
    THREAD = "OFF"
    p, e, t = makeNewBoard(pts)

'''Método para  dibujar, es  el main,  lo que  hace es  inicializar el
board y posteriormente, va a ir actualizandolo con los movimientos.'''
def draw():
    showBoard(p, e)
    if THREAD == "ON":
        updateBoard(pts, p, e)
