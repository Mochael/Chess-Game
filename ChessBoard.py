from tkinter import *
from BackEndChess import *


class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []

    def drawBoard(canvas, self):
        margin = 20
        cellWidth = (self.width-2*margin)//8
        cellHeight = (self.height-2*margin)//8
        for row in range(8):
            if row%2 == 0:
                for col in range(8):
                    if col%2 == 0:
                        canvas.create_rectangle(margin+col*cellWidth, margin+row*cellHeight,
                        margin+(col+1)*cellWidth, margin+(row+1)*cellHeight, fill = "tan",
                        width = cellHeight//25)
                    else:
                        canvas.create_rectangle(margin+col*cellWidth, margin+row*cellHeight,
                        margin+(col+1)*cellWidth, margin+(row+1)*cellHeight, fill = "brown",
                        width = cellHeight//25)
            else:
                for col in range(8):
                    if col%2 == 0:
                        canvas.create_rectangle(margin+col*cellWidth, margin+row*cellHeight,
                        margin+(col+1)*cellWidth, margin+(row+1)*cellHeight, fill = "brown",
                        width = cellHeight//25)
                    else:
                        canvas.create_rectangle(margin+col*cellWidth, margin+row*cellHeight,
                        margin+(col+1)*cellWidth, margin+(row+1)*cellHeight, fill = "tan",
                        width = cellHeight//25)

    def drawPieces(self, board):
        margin = 20
        cellWidth = (self.width-2*margin)//8
        cellHeight = (self.height-2*margin)//8
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                xc = margin+cellWidth*col-cellWidth/2
                yc = margin+cellHeight*row-cellHeight/2
                if self.board[row][col] != None:
                    self.board[row][col].image

    def makeBoard(self):
        self.board = []
        for row in range(8):
            tempB = []
            for col in range(8):
                tempB.append(None)
            self.board.append(tempB)
        for i in range(8):
            self.board[1][i] = Pawn("Black", 1, i)
        for j in range(8):
            self.board[6][j] = Pawn("White", 6, j)
        for k in range(8):
            if k%7 == 0:
                self.board[0][k] = Rook("Black", 0, k)
            elif k == 1 or k == 6:
                self.board[0][k] = Knight("Black", 0, k)
            elif k == 2 or k == 5:
                self.board[0][k] = Bishop("Black", 0, k)
            elif k == 3:
                self.board[0][k] = Queen("Black", 0, k)
            elif k == 4:
                self.board[0][k] = King("Black", 0, k)
        for l in range(8):
            if l%7 == 0:
                self.board[7][l] = Rook("Black", 0, l)
            elif l == 1 or l == 6:
                self.board[7][l] = Knight("Black", 0, l)
            elif l == 2 or l == 5:
                self.board[7][l] = Bishop("Black", 0, l)
            elif l == 3:
                self.board[7][l] = Queen("Black", 0, l)
            elif l == 4:
                self.board[7][l] = King("Black", 0, l)