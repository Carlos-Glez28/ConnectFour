import math
import pygame
import sys
import numpy as np


# BOARD DIMENSIONS
MAXROWS = 6
MAXCOL = 7


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


board = createBoard()
gameOver = False
turn = 0
while not gameOver:
    if turn % 2 == 0:
        column = int(input("Player 1: Make your Selection (0-6):"))
        if isValidLoc(column, board):
            row = getNextOpenRow(column, board)
            dropPiece(board, row, column, 1)
            if checkForConnectFour(board):
                gameOver = True
                print("Player 1 Wins")
    else:
        column = int(input("Player 2: Make your selection (0-6):"))
        if isValidLoc(column, board):
            row = getNextOpenRow(column, board)
            dropPiece(board, row, column, 2)
            if checkForConnectFour(board):
                gameOver = True
                print("Player 2 Wins")
    turn += 1
    printBoard(board)
