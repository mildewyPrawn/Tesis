import random
import Pts as p

DIM = 120
CELLDIM = 5
NUMSEEDS = 50
BOXDIM = 10
MARGIN = (DIM - BOXDIM) / 2

def makeNineActive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            board[i][j] = True

def makeNineInactive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            board[i][j] = False

def makeNeighborsActive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not i==0 or i==DIM-1 or j==0 or j==DIM-1:
                if not i==x and j==y:
                    board[i][j] = True

def makeNeighborsInactive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not i==0 or i==DIM-1 or j==0 or j==DIM-1:
                if not i==x and j==y:
                    board[i][j] = False

# def makeEmptyBoard():
#     return [[False for i in range(DIM)] for j in range(DIM)]

def makeFullBoard():
    return [[True for i in range(DIM)] for j in range(DIM)]

'''Funcion que toma las lineas leidas y regresa una lista de puntos en
forma de tuplas'''
def lines_to_tuples(pts):
    pts_as_tups = []
    for pt in pts:
        tup = pt.strip().split(' ')
        pts_as_tups.append((float(tup[0]), float(tup[1])))
    return pts_as_tups

'''Funcion que  crea el tablero  inicial. Tenemos que  usar isometrias
para relocar los puntos, de otra  forma se ven muy juntos. Actualmente
los voltea.'''
def makeBoards(pts):
    board = pts.get_pts_iso()
    board_two = [(256, 258), (260, 257), (260, 255), (258, 254), (257, 256)]
    return (board, board_two)

'''Funcion que dibuja los bordes. Estos bordes deberian servirnos para
no ir al infinito.'''
def drawBorder():
    stroke(0,255,0)
    line(5, 5, 695, 5);
    line(5, 5, 5, 695);
    line(695, 695, 695, 5);
    line(695, 695, 5, 695);
    # p.hola()

'''Funcion que muestra el tablero, dibuja bolitas en el mapa.'''
def showBoard(board):
    drawBorder() # TODO: crear dinamicamente el borde
    for pt in board:
        x, y = pt
        ellipse(x,y, 5, 5)
    fill(0,0,255)

def sumNine(board, x, y):
    sum = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if board[i][j]:
                sum += 1
    return sum

def sumNeighbors(board, x, y):
    sum = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not i==x and j==y:
                if board[i][j]:
                    sum += 1
    return sum

def updateInerts(boardInerts):
    for i in range(1, DIM-1):
        for j in range(1, DIM-1):
            boardInerts[i][j] = False

def updateBoard(board, boardTwo, boardInerts):
    changes = []
    for i in range(1, DIM-1):
        for j in range(1, DIM-1):
            if boardInerts[i][j]:
                num = sumNine(board, i, j)
                if board[i][j]:
                    if num<3 or num>4:
                        boardTwo[i][j] = False
                        changes.append([False, i, j])
                else:
                    if num==3:
                        boardTwo[i][j] = True
                        changes.append([True, i, j])
    updateInerts(boardInerts)
    for change in changes:
        board[change[1]][change[2]] = change[0]
        makeNineActive(boardInerts, change[1], change[2])

def getCopies(boardCopy):
    board = [row[:] for row in boardCopy]
    boardTwo = [row[:] for row in boardCopy]
    return (board, boardTwo)

def flipState(board, boardTwo, boardInerts, x, y):
    makeNineActive(boardInerts, x, y)
    if board[x][y]:
        board[x][y] = False
        boardTwo[x][y] = False
    else:
        board[x][y] = True
        boardTwo[x][y] = True

def flipLife(board, boardTwo, boardInerts, x, y):
    makeNineActive(boardInerts, x, y)
    board[x][y] = True
    boardTwo[x][y] = True

def flipDeath(board, boardTwo, boardInerts, x, y):
    makeNineActive(boardInerts, x, y)
    board[x][y] = False
    boardTwo[x][y] = False
