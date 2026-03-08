import logging
import random
import os
import sys
from Tesis import *
from Board import *
import Button as btn

MODE = "RANDOM" # RANDOM or USER
THREAD = "OFF" # ON or OFF
PEN = "DRAW" # DRAW or ERASER
FRAMERATE = 1

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("voronoi")

logger.info("Logger intialized.")

# with this i read files
filename = os.environ['FILE']
points = lines_to_points(filename)
pts = Board(points)

'''Metodo reset,  servira para volver  a empeazar le ejecucion  con la
configuracion inicial.'''
def reset():
    global THREAD, p, e, bInert
    THREAD = "OFF"
    p, e, t = makeNewBoard(pts)

'''Metodo para imprimir una configuracion de puntos en formato de tikz'''
def print_tikz():
    print_thesis(pts)

'''Metodo para guardar una configuracion de puntos en formato de .tes'''
def save_frame():
    save_thesis(pts)

def exit_app():
    exit()

def pause_play():
    global THREAD
    print("\u23ef")
    if THREAD == "OFF":
        THREAD = "ON"
    else:
        THREAD = "OFF"

btn_r = btn.Button(10, 10, 20, 23, "r", reset)
btn_p = btn.Button(30, 10, 20, 23, "p", print_tikz)
btn_g = btn.Button(50, 10, 20, 23, "g", save_frame)
btn_q = btn.Button(70, 10, 20, 23, "q", exit_app)
btn_pp = btn.Button(90, 10, 20, 23, unichr(0x23ef), pause_play)

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
    elif key == "p":
        print_tikz()
    elif key == "g":
        save_frame()
    elif key == "q":
        exit()

'''Metodo para  dibujar, es  el main,  lo que  hace es  inicializar el
board y posteriormente, va a ir actualizandolo con los movimientos.'''
def draw():

    pushMatrix()

    showBoard(p, e)
    translate(100, height/2+300)
    scale(1, -1)

    if THREAD == "ON":
        updateBoard(pts, p, e)

    popMatrix()

    btn_r.display()
    btn_p.display()
    btn_g.display()
    btn_q.display()
    btn_pp.display()

def mousePressed():
    btn_r.click()
    btn_p.click()
    btn_g.click()
    btn_q.click()
    btn_pp.click()
