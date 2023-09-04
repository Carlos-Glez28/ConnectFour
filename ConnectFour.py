import math
import pygame
import sys
import numpy as np


# BOARD DIMENSIONS
MAXROWS = 6
MAXCOL = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def createBoard():
    board = np.zeros((MAXROWS, MAXCOL))
    return board


def dropPiece(board, row, column, piece):
    board[row][column] = piece


# Checks if piece dropped is a valid location
def isValidLoc(column, board) -> bool:
    return board[MAXROWS - 1][column] == 0


def getNextOpenRow(column, board) -> int:
    for r in range(MAXROWS):
        if board[r][column] == 0:
            return r


def printBoard(board):
    print(np.flip(board, 0))


# Checks the whole board for a connect four
def checkForConnectFour(board) -> bool:
    for r in range(MAXROWS):
        for c in range(MAXCOL):
            if board[r][c] != 0:
                if checkVerticalFourInARow(board, r, c):
                    return True
                if checkHorizontalFourInARow(board, r,c):
                    return True
                if checkDiagonalFourInARow(board, r, c):
                    return True
    return False


def checkVerticalFourInARow(board, row, column) -> bool:
    count = 0
    win = False
    for r in range(row, MAXROWS):
        if board[r][column] == board[row][column]:
            count += 1
        else:
            break
    if count >= 4:
        win = True
    return win


def checkHorizontalFourInARow(board, row, column) -> bool:
    count = 0
    win = False
    for c in range(column, MAXCOL):
        if board[row][c] == board[row][column]:
            count += 1
        else:
            break
    if count >= 4:
        win = True
    return win


def checkDiagonalFourInARow(board, row, column) -> bool:
    #checks positive diagonal
    c = column
    win = False
    count = 0
    for r in range(row, MAXROWS):
        if c > MAXCOL:
            break
        elif board[r][c] == board[row][column]:
            count += 1
        else:
            break
        c += 1
    if count >= 4:
        win = True
    #checks negative diagonal
    count = 0
    c = column
    for r in range(row, -1, -1):
        if c > MAXCOL:
            break
        elif board[r][c] == board[row][column]:
            count += 1
        else:
            break
        c += 1
    if count >= 4:
        win = True
    return win


def drawBoard(board):
    # Creates board and creates black circles
    for c in range(MAXCOL):
        for r in range(MAXROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    #Creates Animation for user input
    for c in range(MAXCOL):
        for r in range(MAXROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

board = createBoard()
gameOver = False
turn = 0

pygame.init()

SQUARESIZE = 100
width = MAXCOL * SQUARESIZE
height = (MAXROWS + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

font = pygame.font.SysFont("monospace", 75)

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn % 2 == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn % 2 == 0:
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))
                if isValidLoc(column, board):
                    row = getNextOpenRow(column, board)
                    dropPiece(board, row, column, 1)
                    if checkForConnectFour(board):
                        gameOver = True
                        label = font.render("Player 1 Wins", 1, RED)
                        screen.blit(label, (40, 10))
            else:
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))
                if isValidLoc(column, board):
                    row = getNextOpenRow(column, board)
                    dropPiece(board, row, column, 2)
                    if checkForConnectFour(board):
                        gameOver = True
                        label = font.render("Player 2 Wins", 1, YELLOW)
                        screen.blit(label, (40, 10))
            turn += 1
            printBoard(board)
            drawBoard(board)

            if gameOver:
                pygame.time.wait(5000)