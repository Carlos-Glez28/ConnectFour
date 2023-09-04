import math
import pygame
import sys
import numpy as np

#BOARD DIMENSIONS
MAXROWS = 6
MAXCOL = 7

def createBoard():
    board = np.zeros((6, 7))
    return board


def dropPiece(board, row, column, piece):
    board[row][column] = piece

# Checks if piece dropped is a valid location
def isValidLoc(column, board):
    return board[5][column] == 0

def getNextOpenRow(column, board):
    for r in range(MAXROWS):
        if isValidLoc(column, board):
            return r

def printBoard(board):
    print(np.flip(board, 0))
board = createBoard()
gameOver = False
turn = 0
while not gameOver:
    if turn % 2 == 0:
        column = int(input("Player 1: Make your Selection (0-6):"))
        if isValidLoc(column, board):
            row = getNextOpenRow(column, board)
            dropPiece(board, row, column, 1)
    else:
        column = int(input("Player 2: Make your selection (0-6):"))
        if isValidLoc(column, board):
            row = getNextOpenRow(column, board)
            dropPiece(board, row, column, 2)
    turn += 1
    printBoard(board)

