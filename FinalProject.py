# Tutorial mode: animations for user to learn how chess works and what the pieces do (maybe make a youtube video explaining rules).

# Training mode: user plays against AI that tells user why it is making those moves. Maybe in this mode the chess AI can give you a visual display of the succession of moves it plans to make and show you how the paths of the moves change as you make your own moves.

# Competitive mode: user plays AI from different difficulties

# Multiplayer: user can play against different players online

# Difference in AI difficulties could be how far the AI can see into the future with its move predictions.

from tkinter import *
from PIL import Image, ImageTk
import ChessBoard as CB
import BackEndChess as BackEnd
from MultiplayerChess import *

def startScreen(canvas, data):
    canvas.create_text(data.width/2, data.height/4,
                        text = "Welcome to Chess Trainer",
                        font = "courier "+str(int(data.width/25))+" underline")
    canvas.create_text(data.width/2, data.height/2,
                        text = "select one of the below options to begin",
                        font = "courier "+str(int(data.width/30)))
# Modes for player to select.
    canvas.create_rectangle(data.x1-data.r,data.y1-data.r,data.x1+data.r,data.y1+data.r,
                            fill = "grey")
    canvas.create_text(data.x1, data.y1,
                        text = "tutorial \n  mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_rectangle(data.x2-data.r,data.y2-data.r,data.x2+data.r,data.y2+data.r,
                            fill = "grey")
    canvas.create_text(data.x2, data.y2,
                        text = "training \n  mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_rectangle(data.x3-data.r,data.y3-data.r,data.x3+data.r,data.y3+data.r,
                            fill = "grey")
    canvas.create_text(data.x3, data.y3,
                        text = "competitive \n    mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")
    canvas.create_rectangle(data.x4-data.r,data.y4-data.r,data.x4+data.r,data.y4+data.r,
                            fill = "grey")
    canvas.create_text(data.x4, data.y4,
                        text = "multiplayer \n   mode", 
                        font = "courier "+str(int(data.width/44)),
                        fill = "black")

def tutorialScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    canvas.create_text(data.width/2, data.height/2, 
                       text = "Search the link below to watch the tutorial",
                       font = "courier "+str(int(data.width/25)))
    canvas.create_text(data.width/2, data.height*3/4, 
                       text = "https://www.youtube.com/watch?v=t-uwGvx4V_A",
                       font = "courier "+str(int(data.width/30)))
    
def trainingScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    if data.mainBoard.clicked:
        canvas.create_rectangle(data.mainBoard.margin+data.mainBoard.colClick*data.mainBoard.cellWidth,
                                data.mainBoard.margin+data.mainBoard.rowClick*data.mainBoard.cellHeight,
                                data.mainBoard.margin+(data.mainBoard.colClick+1)*data.mainBoard.cellWidth,
                                data.mainBoard.margin+(data.mainBoard.rowClick+1)*data.mainBoard.cellHeight,
                                fill = "yellow")
    initialize(canvas, data)
    drawImages(canvas, data)

def competitiveScreen(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='white', width=0)
    data.mainBoard.drawBoard(canvas)
    canvas.create_text(15, 15, 
                       text = "Back",
                       font = "courier "+str(int(data.width/25)))
    if data.mainBoard.clicked:
        canvas.create_rectangle(data.mainBoard.margin+data.mainBoard.colClick*data.mainBoard.cellWidth,
                                data.mainBoard.margin+data.mainBoard.rowClick*data.mainBoard.cellHeight,
                                data.mainBoard.margin+(data.mainBoard.colClick+1)*data.mainBoard.cellWidth,
                                data.mainBoard.margin+(data.mainBoard.rowClick+1)*data.mainBoard.cellHeight,
                                fill = "yellow")
    initialize(canvas, data)
    drawImages(canvas, data)


def gameMode(event, data):
    if data.mode != "beginning":
        if 0 <= event.x <= 30:
            if 0 <= event.y <= 30:
                init(data)
    else:
        if data.x1-data.r <= event.x <= data.x1+data.r:
            if data.y1-data.r <= event.y <= data.y1+data.r:
                data.mode = "tutorial"
        if data.x2-data.r <= event.x <= data.x2+data.r:
            if data.y2-data.r <= event.y <= data.y2+data.r:
                data.mode = "training"
        if data.x3-data.r <= event.x <= data.x3+data.r:
            if data.y3-data.r <= event.y <= data.y3+data.r:
                data.mode = "competitive"
        if data.x4-data.r <= event.x <= data.x4+data.r:
            if data.y4-data.r <= event.y <= data.y4+data.r:
                data.mode = "multiplayer"

def moveWithMouse(event, data):
    if data.mainBoard.clicked:
        if data.mode == "training":
            data.mainBoard.moveClick(event.x, event.y, data.player)
            data.player = data.mainBoard.turn
        else:
            data.mainBoard.moveClick(event.x, event.y, data.player)
    else:
        data.mainBoard.mouseClick(event.x, event.y, data.player)


####################################
# customize these functions
####################################

def init(data):
    data.mode = "beginning"
    data.x1 = data.width/19*2
    data.y1 = data.height/4*3
    data.x2 = data.width/20*7
    data.y2 = data.height/4*3
    data.x3 = data.width/20*12
    data.y3 = data.height/4*3
    data.x4 = data.width/19*16
    data.y4 = data.height/4*3
    data.r = 50
    data.mainBoard = CB.Board(data.width, data.height)
    data.mainBoard.makeBoard()
    data.player = "White"

def initialize(canvas, data):
    canvas.shapes = data.mainBoard.drawings

def drawImages(canvas, data):
    for key in canvas.shapes:
        im = Image.open(canvas.shapes[key])
        im = im.resize((data.width//5-2*data.mainBoard.margin, data.height//5-2*data.mainBoard.margin), 
                        Image.ANTIALIAS)
        ph = ImageTk.PhotoImage(im)
        label = Label(canvas, image=ph)
        label.image=ph  #need to keep the reference of your image to avoid garbage collection
        canvas.create_image(int(key[1]*data.mainBoard.cellWidth+data.mainBoard.cellWidth*(19/20)), 
                            int(key[0]*data.mainBoard.cellHeight+data.mainBoard.cellHeight*(19/20)),
                            image=ph)

def mousePressed(event, data):
    if data.mode != "beginning":
        moveWithMouse(event, data)
    gameMode(event, data)


def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.mode == "beginning":
        startScreen(canvas, data)

    if data.mode == "tutorial":
        tutorialScreen(canvas, data)

    if data.mode == "training":
        trainingScreen(canvas, data)

    if data.mode == "competitive":
        competitiveScreen(canvas, data)

    if data.mode == "multiplayer":
        multiplayerScreen(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10000 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    initialize(canvas, data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)