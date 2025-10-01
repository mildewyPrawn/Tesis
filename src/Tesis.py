import itertools
import heapq
import random
import Point as pt
import Edge as ed
import Circle as cr
import logging

DIM = 120
CELLDIM = 5
NUMSEEDS = 50
BOXDIM = 10
MARGIN = (DIM - BOXDIM) / 2

logger = logging.getLogger('Tesis')

def makeFullBoard():
    return [[True for i in range(DIM)] for j in range(DIM)]

'''Funcion que toma las lineas leidas y regresa una lista de puntos en
forma de tuplas'''
def lines_to_tuples(pts):
    pts_as_tups = []
    for pt in pts:
        tup = pt.strip().split(' ')
        pts_as_tups.append((float(tup[0]), float(tup[1])))
        logger.info('Puntos leidos: {}'.format(pts_as_tups))
    return pts_as_tups

'''Funcion que  crea el tablero  inicial. Tenemos que  usar isometrias
para relocar los puntos, de otra  forma se ven muy juntos. Actualmente
los voltea.'''
def makeBoards(pts):
    board = pts.get_pts_iso()
    edges = pts.get_vor_edges()
    return (board, edges)

'''Metodo que crea un nuevo tablero (Resetea los puntos).'''
def makeNewBoard(pts):
    return pts.reset()

'''Funcion que dibuja los bordes. Estos bordes deberian servirnos para
no ir al infinito.'''
def drawBorder():
    stroke(0,0,255)
    line(5, 5, 695, 5);
    line(5, 5, 5, 695);
    line(695, 695, 695, 5);
    line(695, 695, 5, 695);

'''Funcion que muestra el tablero, dibuja bolitas en el mapa.'''
def showBoard(points, edges):
    drawBorder()

'''Metodo que actualiza  el tablero, con los puntos y  aristas que hay
que dibujar'''
def updateBoard(board, points, edges):
    background(0)
    board.randomize()
    e = board.drawLines()
    p = board.drawPoints()
    logger.info('Update Board: <points {}>, <edges {}>'.format(p, e))

def print_thesis(board):
    logger.info('Draw tikz.')
    board.print_thesis_in_tikz()

def save_thesis(board):
    logger.info('Save frame.')
    board.save_thesis()
