from tkinter import *
from BackEndChess import *

def drawBoard(canvas, width, height):
    margin = 20
    cellWidth = (width-2*margin)//8
    cellHeight = (height-2*margin)//8
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

def makeBoard():
    board = []
    for row in range(8):
        tempB = []
        for col in range(8):
            tempB.append(None)
        board.append(tempB)
    for i in range(8):
        board[1][i] = Pawn("Black", 1, i)
    for j in range(8):
        board[6][j] = Pawn("White", 6, j)
    for k in range(8):
        if k%7 == 0:
            board[0][k] = Rook("Black", 0, k)
        elif k == 1 or k == 6:
            board[0][k] = Knight("Black", 0, k)
        elif k == 2 or k == 5:
            board[0][k] = Bishop("Black", 0, k)
        elif k == 3:
            board[0][k] = Queen("Black", 0, k)
        elif k == 4:
            board[0][k] = King("Black", 0, k)
    for l in range(8):
        if l%7 == 0:
            board[7][l] = Rook("Black", 0, l)
        elif l == 1 or l == 6:
            board[7][l] = Knight("Black", 0, l)
        elif l == 2 or l == 5:
            board[7][l] = Bishop("Black", 0, l)
        elif l == 3:
            board[7][l] = Queen("Black", 0, l)
        elif l == 4:
            board[7][l] = King("Black", 0, l)
    print(board[1][0].color)
    print(board[1][0].posRow)
    print(board[1][0].posCol)
    print(board[1][0].getMoves(board))
    print(board[1][0].moves)




def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    drawBoard(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(400, 400)
makeBoard()