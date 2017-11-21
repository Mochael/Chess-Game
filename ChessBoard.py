from tkinter import *
from BackEndChess import *
import copy

class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.margin = 20
        self.cellWidth = (self.width-2*self.margin)//8
        self.cellHeight = (self.height-2*self.margin)//8
        self.board = []
        self.clicked = False
        self.rowClick = None
        self.colClick = None
        self.drawings = {}
        self.turn = "White"

    def drawBoard(self, canvas):
        for row in range(8):
            if row%2 == 0:
                for col in range(8):
                    if col%2 == 0:
                        canvas.create_rectangle(self.margin+col*self.cellWidth, self.margin+row*self.cellHeight,
                        self.margin+(col+1)*self.cellWidth, self.margin+(row+1)*self.cellHeight, fill = "tan",
                        width = self.cellHeight//25)
                    else:
                        canvas.create_rectangle(self.margin+col*self.cellWidth, self.margin+row*self.cellHeight,
                        self.margin+(col+1)*self.cellWidth, self.margin+(row+1)*self.cellHeight, fill = "brown",
                        width = self.cellHeight//25)
            else:
                for col in range(8):
                    if col%2 == 0:
                        canvas.create_rectangle(self.margin+col*self.cellWidth, self.margin+row*self.cellHeight,
                        self.margin+(col+1)*self.cellWidth, self.margin+(row+1)*self.cellHeight, fill = "brown",
                        width = self.cellHeight//25)
                    else:
                        canvas.create_rectangle(self.margin+col*self.cellWidth, self.margin+row*self.cellHeight,
                        self.margin+(col+1)*self.cellWidth, self.margin+(row+1)*self.cellHeight, fill = "tan",
                        width = self.cellHeight//25)
        self.drawPieces(canvas)

    def drawPieces(self, canvas):
        self.margin = 20
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                xc = self.margin+self.cellWidth*col-self.cellWidth/2
                yc = self.margin+self.cellHeight*row-self.cellHeight/2
                if self.board[row][col] != None:
                    self.drawings[(row,col)] = self.board[row][col].image
                    #photo = ImageTk.PhotoImage(Image.open(self.board[row][col].image))
                    #canvas.create_image(xc, yc, image = photo)

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
                self.board[7][l] = Rook("White", 0, l)
            elif l == 1 or l == 6:
                self.board[7][l] = Knight("White", 0, l)
            elif l == 2 or l == 5:
                self.board[7][l] = Bishop("White", 0, l)
            elif l == 3:
                self.board[7][l] = Queen("White", 0, l)
            elif l == 4:
                self.board[7][l] = King("White", 0, l)

    def mouseClick(self, eventX, eventY, player):
        if self.turn == player:
            if (self.margin <= eventX <= self.width-self.margin and 
            self.margin <= eventY <= self.height-self.margin):
                self.rowClick = int((eventY-self.margin)/((self.height-2*self.margin)/8))
                self.colClick = int((eventX-self.margin)/((self.width-2*self.margin)/8))
                if self.board[self.rowClick][self.colClick] != None and self.board[self.rowClick][self.colClick].color == player:
                    print("yeeehaw")
                    self.clicked = True

# Run moveClick before mouseClick and only run if self.clicked = True.
    def moveClick(self, eventX, eventY, player):
        rowMove = int((eventY-self.margin)/((self.height-2*self.margin)/8))
        colMove = int((eventX-self.margin)/((self.width-2*self.margin)/8))
        if self.board[rowMove][colMove] == None or self.board[rowMove][colMove].color != player:
            self.board[self.rowClick][self.colClick].getMoves
            if [rowMove, colMove] in self.board[self.rowClick][self.colClick].moves:
                tempB = copy.deepcopy(self.board)
                tempB[rowMove][colMove] = tempB[self.rowClick][self.colClick]
                tempB[self.rowClick][self.colClick] = None
                if not isCheck(tempB, turn):
                    self.board[rowMove][colMove] = self.board[self.rowClick][self.colClick]
                    self.board[self.rowClick][self.colClick] = None
            if self.turn == "White":
                self.turn = "Black"
            else:
                self.turn = "White"
        self.clicked = False
        self.rowClick = None
        self.colClick = None
        
            # Set rowClick and colClick back to None after turn ends
                    