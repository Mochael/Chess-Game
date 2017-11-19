from tkinter import *

def drawBoard(canvas, width, height):
    margin = 10
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


def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    drawBoard(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(400, 400)